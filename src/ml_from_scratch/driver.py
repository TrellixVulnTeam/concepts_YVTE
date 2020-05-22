"""
Basically import modules and test their individual methods whether they work fine.
Later this will help to build a suite of testcases.
"""

from ml_from_scratch import neural_network as nn


if __name__ == '__main__':
    net = nn.initialize_network(2,1, 2)
    nn.print_network(net)