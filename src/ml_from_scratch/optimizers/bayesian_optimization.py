"""
Reference: https://machinelearningmastery.com/what-is-bayesian-optimization/

Key points:
    1.

Tutorial Overview:
    1. Challenges of Functional Optimization
    2. What is Bayesian Optimization
    3. How to Perform Bayesian Optimization
    4. Hyper-parameter Tuning with Bayesian Optimization

Summary of optimization in machine learning:
    1. Algorithm Training: Optimization of model parameters.
    2. Algorithm Tuning: Optimization of model hyperparameters.
    3. Predictive Modeling: Optimization of data, data preparation, and algorithm selection.
"""

# example of the test problem
from math import sin, pi
from numpy import arange, argmax
from numpy.random import normal
from matplotlib import pyplot as plt


# objective function
def objective(x, noise=0.1):
    noise = normal(loc=0, scale=noise)
    return (x ** 2 * sin(5 * pi * x) ** 6.0) + noise


def test_problem():
    # grid-based sample of the domain [0,1]
    X = arange(0, 1, 0.01)
    # sample the domain without noise
    y = [objective(x, 0) for x in X]
    # sample the domain with noise
    ynoise = [objective(x) for x in X]
    # find best result
    ix = argmax(y)
    print('Optima: x=%.3f, y=%.3f' % (X[ix], y[ix]))
    # plot the points with noise
    plt.scatter(X, ynoise)
    # plot the points without noise
    plt.plot(X, y)
    # show the plot
    plt.show()


def main():
    test_problem()


if __name__ == '__main__':
    main()
