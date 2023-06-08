import argparse
from utils import *
from model import DySAT


def get_parameters():
    parser = argparse.ArgumentParser(description='prediction algorithm')
    parser.add_argument('--enable_cuda', type=bool, default=True, help='enable CUDA, default as True')
    parser.add_argument('--seed', type=int, default=42, help='set the random seed for stabilizing experiment results')
    parser.add_argument('--lr', type=float, default=0.01, help='learning rate')
    parser.add_argument('--weight_decay_rate', type=float, default=0.005, help='weight decay (L2 penalty)')
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--epochs', type=int, default=10, help='epochs, default as 10000')
    parser.add_argument('--opt', type=str, default='adam', help='optimizer, default as adam')
    args = parser.parse_args()
    print('Training configs: {}'.format(args))
    return args


if __name__ == "__main__":
    config_path = "/home/xuexun/Desktop/code/DL4HM/models/cc/config.properties"

    args = get_parameters()
    set_environment(seed=args.seed)
    logger = config_logger("./run.log")
    config = read_properties(config_path)