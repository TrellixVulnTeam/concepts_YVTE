"""
This module is a practice module to understand how to solve IMBALANCED CLASS machine learning problem
Ref: https://machinelearningmastery.com/imbalanced-classification-model-to-detect-oil-spills/
"""

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
from numpy import mean
from numpy import std
from pandas import read_csv
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from imblearn.metrics import geometric_mean_score
from sklearn.metrics import make_scorer
from sklearn.dummy import DummyClassifier


def plot_hist(df):
    ax = df.hist()

    # Disable axis title and labels to avoid clutter
    for axis in ax.flatten():
        axis.set_title('')
        axis.set_xticklabels([])
        axis.set_yticklabels([])
    plt.show()


def summarize_data(df, num_target_col):
    # summarize the shape of the dataset
    print(f"Shape: {df.shape}")

    # summarize the class distribution
    target = df.values[:, num_target_col]
    counter = Counter(target)
    for k, v in counter.items():
        per = v / len(target) * 100
        print('Class=%d, Count=%d, Percentage=%.3f%%' % (k, v, per))


def read_data(file_path, header=None):
    df = pd.read_csv(file_path, header=header)
    return df


def load_dataset(full_path):
    # load the dataset as a numpy array
    data = pd.read_csv(full_path, header=None)
    # drop unused columns
    data.drop(22, axis=1, inplace=True)
    data.drop(0, axis=1, inplace=True)
    # retrieve numpy array
    data = data.values
    # split into input and output elements
    X, y = data[:, :-1], data[:, -1]
    # label encode the target variable to have the classes 0 and 1
    y = LabelEncoder().fit_transform(y)
    return X, y


def main():
    file_path = f"../data/oil_spill/oil-spill.csv"
    df = read_data(file_path)
    summarize_data(df, -1)
    plot_hist(df)


if __name__ == '__main__':
    main()
