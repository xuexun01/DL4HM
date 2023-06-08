import glob

import networkx as nx
import numpy as np
import pandas as pd
import scipy.sparse as sp
import torch
import torch_geometric
from torch.utils.data import DataLoader, Dataset
from torch_geometric.data import Data, Batch
from tqdm import *


class ODMatrixDataset(Dataset):
    def __init__(self, filepath):
        super(ODMatrixDataset, self).__init__()
        self.graphs = self._get_graphs(filepath)
        time_steps = len(self.graphs)

        adjs = [nx.adjacency_matrix(graph) for graph in self.graphs]
        features = [sp.identity(adjs[time_steps - 1].shape[0]).tocsr()[range(0, x.shape[0]), :] for x in adjs if x.shape[0] <= adjs[time_steps - 1].shape[0]]

        self.features = [self._preprocess_features(feature) for feature in features]
        self.adj_mats = [self._normalize_graph_gcn(graph)  for graph  in self.graphs]

        self.time_steps = time_steps
        # all nodes in the graph.
        self.train_nodes = list(self.graphs[self.time_steps-1].nodes())
        self.pyg_graphs = self._build_pyg_graphs()

    def __len__(self):
        return len(self.graphs)

    def __getitem__(self, index):
        item = {}
        item['pyg_graphs'] = self.pyg_graphs
        item['nodes'] = self.train_nodes
        item['graphs'] = self.graphs
        return item
    
    def _get_graphs(self, filepath):
        files = glob.glob(filepath + "/*.xlsx")
        graphs = []
        nodes = pd.read_excel(files[0], index_col=0)
        for file in files:
            dataframe = pd.read_excel(file, index_col=0)
            graph = nx.DiGraph()
            for i in range(len(dataframe.index)):
                for j in range(len(dataframe.columns)):
                    # 如果元素为0，则跳过
                    if abs(dataframe.iloc[i, j] - 0) < 0.01:
                        continue
                    # 将起点和终点转换为节点名称，并添加一条边
                    start_node = dataframe.index[i]
                    end_node = dataframe.columns[j]
                    graph.add_edge(start_node, end_node, weight=dataframe.iloc[i, j])
            graphs.append(graph)
        return graphs
    
    def _normalize_graph_gcn(self, graph):
        adj = nx.adjacency_matrix(graph)
        """GCN-based normalization of adjacency matrix (scipy sparse format). Output is in tuple format"""
        adj = sp.coo_matrix(adj, dtype=np.float32)
        adj_ = adj + sp.eye(adj.shape[0], dtype=np.float32)
        rowsum = np.array(adj_.sum(1), dtype=np.float32)
        degree_mat_inv_sqrt = sp.diags(np.power(rowsum, -0.5).flatten(), dtype=np.float32)
        adj_normalized = adj_.dot(degree_mat_inv_sqrt).transpose().dot(degree_mat_inv_sqrt).tocoo()
        return adj_normalized

    def _preprocess_features(self, features):
        """Row-normalize feature matrix and convert to tuple representation"""
        features = np.array(features.todense())
        rowsum = np.array(features.sum(1))
        r_inv = np.power(rowsum, -1).flatten()
        r_inv[np.isinf(r_inv)] = 0.
        r_mat_inv = sp.diags(r_inv)
        features = r_mat_inv.dot(features)
        return features
    
    def _build_pyg_graphs(self):
        pyg_graphs = []
        for feature, adj_mat in zip(self.features, self.adj_mats):
            x = torch.Tensor(feature)
            edge_index, edge_weight = torch_geometric.utils.from_scipy_sparse_matrix(adj_mat)
            data = Data(x=x, edge_index=edge_index, edge_weight=edge_weight)
            pyg_graphs.append(data)
        return pyg_graphs

    @staticmethod
    def collate_fn(samples):
        batch_dict = {}
        batch_dict["graphs"] = samples[0]["graphs"]
        batch_dict['pyg_graphs'] = samples[0]['pyg_graphs']
        batch_dict['nodes'] = samples[0]['nodes']
        return batch_dict


if __name__ == "__main__":
    filepath = "/home/xuexun/Desktop/code/DL4HM/dataset/mobility/flow_in/"
    mydataset = ODMatrixDataset(filepath)

    # for graph in mydataset.graphs:
    #     print(graph.nodes())
    #     print(nx.adjacency_matrix(graph).todense())
    #     # print(graph.edges(data=True))

    # print(mydataset.train_nodes)
    # for i in mydataset.pyg_graphs:
    #     print(i)
    # print(mydataset.pyg_graphs)


    dataloader = DataLoader(dataset=mydataset, batch_size=2, shuffle=False, collate_fn=mydataset.collate_fn)
    for item in tqdm(dataloader):
        nodes = item['nodes']
        graphs = item['graphs']
        pyg_graphs = item['pyg_graphs']
        print(nodes)
        print(graphs)
        print(pyg_graphs)
