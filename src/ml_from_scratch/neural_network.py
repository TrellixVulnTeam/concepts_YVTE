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

_ROUND_PRECISION = 16
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


def forward_propagate(network, row_x, **kwargs) -> list:
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


def transfer_derivative(output):
    """
    This function implements derivative of sigmoid function.
    Need to understand the steps of derivative and apply it for other functions.
    As the activation transfer function changes, derivative also needs to change.
    @param output:
    @return:
    """
    derivative = output * (1.0 - output)
    derivative = round(derivative, _ROUND_PRECISION)
    return derivative


def back_propagate_error(network, expected):
    """
    This will calculate the backward propagated errors from the expected output and stores in neurons
    @param network: list of layers where a layer is a list of neurons
    @param expected: list of expected values at the output layer
    @return:
    """
    for ith in reversed(range(len(network))):
        layer = network[ith]
        errors = list()
        if ith == len(network) - 1:
            # This part is implemented for the output layer
            for jth in range(len(layer)):
                neuron = layer[jth]
                errors.append(expected[jth] - neuron['output'])
        else:
            # This is for the hidden layers
            # Here the error is based upon it's contribution to the next layer's neuron's outputs
            # Hence, weighted error back propagation
            for jth in range(len(layer)):
                weighted_error = 0.0
                for neuron in network[ith + 1]:
                    weighted_error += (neuron['weights'][jth] * neuron['delta'])
                errors.append(weighted_error)
        for kth in range(len(layer)):
            neuron = layer[kth]
            neuron['delta'] = errors[kth] * transfer_derivative(neuron['output'])
    return network


def update_weights(network, row, learn_rate):
    """
    This basically updates the weights by using the neuron['delta'] that is calculated after the back-prop step.
    @param network:
    @param row:
    @param learn_rate:
    @return:
    """
    for ith in range(len(network)):
        inputs = row[:-1]
        if ith != 0:
            inputs = [neuron['output'] for neuron in network[ith]]
        for neuron in network[ith]:
            for jth in range(len(inputs)):
                neuron['weights'][jth] += learn_rate * neuron['delta'] * inputs[jth]
            neuron['weights'][-1] += learn_rate * neuron['delta']


def train_network(network, train, learn_rate, n_epoch, n_outputs):
    """

    Training of network has two steps:
    1. Updating the model weights based on input
    2. Doing it repeatedly

    @param network:
    @param train:
    @param learn_rate:
    @param n_epoch:
    @param n_outputs:
    @return:
    """
    for epoch in range(n_epoch):
        sum_errors = 0.0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for i in range(n_outputs)]
            expected[row[-1]] = 1
            sum_errors += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
            back_propagate_error(network, expected)
            update_weights(network, row, learn_rate)
        print(f"epoch: {epoch}, learn_rate: {learn_rate}, error: {sum_errors}")


def predict():
    pass


def case_study():
    pass
