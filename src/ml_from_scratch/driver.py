"""
Basically import modules and test their individual methods whether they work fine.
Later this will help to build a suite of testcases.
"""

from ml_from_scratch import neural_network as nn


def test_initialize_network():
    net = nn.initialize_network(2, 1, 2)
    nn.print_network(net)


def test_forward_propagate():
    network = [[{'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],
               [{'weights': [0.2550690257394217, 0.49543508709194095]},
                {'weights': [0.4494910647887381, 0.651592972722763]}]]
    row = [1, 0, None]
    output = nn.forward_propagate(network, row)
    print(output)
    assert output == [round(x, 3) for x in [0.6629970129852887, 0.7253160725279748]]


if __name__ == '__main__':
    # test_initialize_network()
    test_forward_propagate()
