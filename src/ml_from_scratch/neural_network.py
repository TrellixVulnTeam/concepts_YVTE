"""
This module will implement neural network from scratch with Back Propagation:
1. Forward-propagation to calculate the error/loss
2. Gradient
3. Back propagation to update the weights

Modelling as Classification problem:
1. Tutorial link: https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/
2. Dataset link: http://archive.ics.uci.edu/ml/datasets/seeds

More resources:
1. http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/
2. https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6

"""

from random import random, seed

_ROUND_PRECISION = 3
_RANDOM_SEED = 1
seed(_RANDOM_SEED)


def print_network(neural_network):
    """
    Takes input a list of layers
    @param neural_network:
    @return:
    """
    for layer in neural_network:
        print(layer)


def initialize_network(n_inputs, n_hidden, n_outputs):
    """
    Create an initial network initialized with random weights in range [0, 1].
    @param n_inputs: feature size
    @param n_hidden: one hidden layer n_hidden neurons. Each neuron has (n_inputs) training weights and 1 bias weight
    @param n_outputs: n_output classes. Each output neuron has (n_hidden) weights and 1 bias weight
    @return:
    """
    netowrk = list()
    # input_layer is just a list of n_inputs values
    hidden_layer = [{'weights': [round(random(), _ROUND_PRECISION)
                                 for x in range(n_inputs + 1)]}
                    for x in range(n_hidden)]
    netowrk.append(hidden_layer)

    # Create output layer
    output_layer = [{'weights': [round(random(), _ROUND_PRECISION)
                                 for x in range(n_hidden + 1)]}
                    for x in range(n_outputs)]
    netowrk.append(output_layer)
    return netowrk


def forward_propagate(x, y):
    """

    @param x:
    @param y:
    @return:
    """


def back_propagate_error():
    pass


def train_network():
    pass


def predict():
    pass


def case_study():
    pass
