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

from math import exp
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


def activate(weights: list, inputs: list, **kwargs):
    """
    This will calculate the dot product of weights and inputs and add a bias value.
    In our case, bias is always assumed to be the last value in the weights list.
    @param weights:
    @param inputs:
    @return:
    """
    # Initialize the sum with bias.
    round_precision = kwargs.get("round_precision", _ROUND_PRECISION)
    activation = weights[-1]
    for i, x_i in enumerate(inputs):
        if x_i is not None:
            activation += x_i * weights[i]

    activation = round(activation, round_precision)
    return activation


def transfer(activation, **kwargs):
    """
    This is basically the output of the dot product.
    The activation is a linear transformation. Now we'll be feeding it to get a non-linear output.
    @param activation:
    @return:
    """
    # TODO: Add various options for transfer functions sigmoid, tanh, relu, etc.
    # We're implementing sigmoid here.
    round_precision = kwargs.get("round_precision", _ROUND_PRECISION)
    transfer_value = round(1.0 / (1.0 + exp(-activation)), round_precision)
    return transfer_value


def forward_propagate(network, row_x, **kwargs):
    """
    It has three steps:
    1. Neuron Activation
    2. Neuron Transfer
    3. Forward propagation

    @param network:
    @param row_x:
    @param kwargs:
    @return:
    """
    output_history = kwargs.get("output_history", "last")
    all_layer_outputs = []
    for layer in network:
        layer_output = []

        for neuron in layer:
            # row_x is original input row initially
            activation = activate(neuron['weights'], row_x)

            # Save the output of this neuron (?)
            neuron['output'] = transfer(activation)
            layer_output.append(neuron['output'])

        # Track the history of activations (just in case you want to study more)
        # We can add a variation here to return outputs of some particular hidden layer based on name/order number
        all_layer_outputs.append(layer_output)

        # As we progress the computations it is updated to the recent layer outputs to feed as input to next layer
        row_x = layer_output.copy()

    if output_history == 'last':
        return all_layer_outputs[-1]
    else:
        return all_layer_outputs


def back_propagate_error():
    pass


def train_network():
    pass


def predict():
    pass


def case_study():
    pass
