import torch
import torch.nn as nn
from layer import StructuralAttentionLayer, TemporalAttentionLayer
import networkx as nx


class DySAT(nn.Module):
    def __init__(self, config, num_features, time_length):
        super(DySAT, self).__init__()
        self.config = config
        if int(config['window']) < 0:
            self.num_time_steps = time_length
        else:
            self.num_time_steps = min(time_length, int(config['window']) + 1)  # window = 0 => only self.
        self.num_features = num_features
        self.structural_head_config = list(map(int, config['structural_head_config'].split(",")))
        self.structural_layer_config = list(map(int, config['structural_layer_config'].split(",")))
        self.temporal_head_config = list(map(int, config['temporal_head_config'].split(",")))
        self.temporal_layer_config = list(map(int, config['temporal_layer_config'].split(",")))
        self.spatial_drop = config['spatial_drop']
        self.temporal_drop = config['temporal_drop']
        self.structural_attn, self.temporal_attn = self.build_model()
        self.result = nn.Linear(self.temporal_layer_config*2, 1)


    def forward(self, graphs):

        # Structural Attention forward
        structural_out = []
        for t in range(0, self.num_time_steps):
            structural_out.append(self.structural_attn(graphs[t]))
        structural_outputs = [g.x[:,None,:] for g in structural_out] # list of [Ni, 1, F]
        # padding outputs along with Ni
        maximum_node_num = structural_outputs[-1].shape[0]
        out_dim = structural_outputs[-1].shape[-1]
        structural_outputs_padded = []
        for out in structural_outputs:
            zero_padding = torch.zeros(maximum_node_num-out.shape[0], 1, out_dim).to(out.device)
            padded = torch.cat((out, zero_padding), dim=0)
            structural_outputs_padded.append(padded)
        structural_outputs_padded = torch.cat(structural_outputs_padded, dim=1) # [N, T, F]
        # Temporal Attention forward
        temporal_out = self.temporal_attn(structural_outputs_padded)
        
        return temporal_out


    def build_model(self):
        input_dim = self.num_features

        # 1: Structural Attention Layers
        structural_attention_layers = nn.Sequential()
        for i in range(len(self.structural_layer_config)):
            layer = StructuralAttentionLayer(input_dim=input_dim,
                                             output_dim=self.structural_layer_config[i],
                                             n_heads=self.structural_head_config[i],
                                             attn_drop=self.spatial_drop,
                                             ffd_drop=self.spatial_drop,
                                             residual=self.config.residual)
            structural_attention_layers.add_module(name="structural_layer_{}".format(i), module=layer)
            input_dim = self.structural_layer_config[i]
        
        # 2: Temporal Attention Layers
        input_dim = self.structural_layer_config[-1]
        temporal_attention_layers = nn.Sequential()
        for i in range(len(self.temporal_layer_config)):
            layer = TemporalAttentionLayer(input_dim=input_dim,
                                           n_heads=self.temporal_head_config[i],
                                           num_time_steps=self.num_time_steps,
                                           attn_drop=self.temporal_drop,
                                           residual=self.config.residual)
            temporal_attention_layers.add_module(name="temporal_layer_{}".format(i), module=layer)
            input_dim = self.temporal_layer_config[i]
    
        return structural_attention_layers, temporal_attention_layers
    

    def get_flow(self, nodes, graphs):
        # run gnn
        final_emb = self.forward(graphs) # [N, T, F]
        results = []
        for t in range(self.num_time_steps - 1):
            emb_t = final_emb[:, t, :].squeeze() #[N, F]
            graph = nx.DiGraph()
            for origin_node in nodes:
                for dest_node in nodes:
                    if origin_node == dest_node:
                        graph.add_edge(origin_node, dest_node, weight=0)
                        continue
                    x = torch.cat((emb_t[origin_node], emb_t[dest_node]), dim=1)
                    flow = self.result(x)
                    graph.add_edge(origin_node, dest_node, weight=flow)
        results.append(graph)
        return results
    

    def predict(time_step = 5):
        results = []
        for i in range(0, time_step):
            pass
        return results