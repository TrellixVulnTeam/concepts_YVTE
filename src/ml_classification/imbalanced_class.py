"""
This module is a practice module to understand how to solve IMBALANCED CLASS machine learning problem
Ref: https://machinelearningmastery.com/imbalanced-classification-model-to-detect-oil-spills/
"""

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter


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


def main():
    file_path = f"../data/oil_spill/oil-spill.csv"
    df = read_data(file_path)
    summarize_data(df, -1)
    plot_hist(df)


if __name__ == '__main__':
    main()
