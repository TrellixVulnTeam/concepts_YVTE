"""
This module is a practice module to understand how to solve IMBALANCED CLASS machine learning problem
Ref: https://machinelearningmastery.com/imbalanced-classification-model-to-detect-oil-spills/
"""

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
from numpy import mean, std

# Useful imports for creating preprocessing classes
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, PowerTransformer
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
from sklearn.pipeline import Pipeline

# Import various models
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB

# Metrics for performance
from sklearn.metrics import make_scorer

# Imports from imblearn - Special package for Imbalanced Classes
from imblearn.metrics import geometric_mean_score
from imblearn.combine import SMOTEENN
from imblearn.under_sampling import EditedNearestNeighbours
from imblearn.pipeline import Pipeline as imb_pipe


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


def evaluate_model(X, y, model):
    # define evaluation procedure
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

    # define the model evaluation metric
    metric = make_scorer(geometric_mean_score)

    # evaluate model
    scores = cross_val_score(model, X, y, scoring=metric, cv=cv, n_jobs=-1)
    return scores


def load_dataset(full_path):
    # load the dataset as a numpy array
    data = pd.read_csv(full_path, header=None)

    # drop unused columns
    list_cols_to_drop = [22, 0]
    for num_col in list_cols_to_drop:
        data.drop(num_col, axis=1, inplace=True)

    # retrieve numpy array
    data = data.values

    # split into input and output elements
    # 2D array indexing: [start:end, start:end]
    # Training data X -> all except the last value in each row
    # Target y -> last element from all the rows -> list
    X, y = data[:, :-1], data[:, -1]

    # label encode the target variable to have the classes 0 and 1
    y = LabelEncoder().fit_transform(y)
    return X, y


def dummy_classifier(X, y):
    # define the reference model
    model = DummyClassifier(strategy='uniform')

    # evaluate the model
    scores = evaluate_model(X, y, model)

    # summarize performance
    print('Mean G-Mean: %.3f (%.3f)' % (mean(scores), std(scores)))


def get_improved_LR_models():
    models, names, results = list(), list(), list()
    # LR Balanced
    models.append(LogisticRegression(solver='liblinear', class_weight='balanced'))
    names.append('LR - Bal')
    # LR Balanced + Normalization
    models.append(
        Pipeline(steps=[('t', MinMaxScaler()), ('m', LogisticRegression(solver='liblinear', class_weight='balanced'))]))
    names.append('LR - Bal - Norm')
    # LR Balanced + Standardization
    models.append(Pipeline(
        steps=[('t', StandardScaler()), ('m', LogisticRegression(solver='liblinear', class_weight='balanced'))]))
    names.append('LR - Bal - Std')
    # LR Balanced  + Power
    models.append(Pipeline(steps=[('t1', MinMaxScaler()), ('t2', PowerTransformer()),
                                  ('m', LogisticRegression(solver='liblinear', class_weight='balanced'))]))
    names.append('LR - Bal - Power')

    # SMOTEENN
    models.append(imb_pipe(steps=[('e', SMOTEENN(enn=EditedNearestNeighbours(sampling_strategy='majority'))),
                                  ('m', LogisticRegression(solver='liblinear'))]))
    names.append('LR - SE')

    # SMOTEENN + Norm
    models.append(imb_pipe(
        steps=[('t', MinMaxScaler()), ('e', SMOTEENN(enn=EditedNearestNeighbours(sampling_strategy='majority'))),
               ('m', LogisticRegression(solver='liblinear'))]))
    names.append('LR - Norm - SE')

    # SMOTEENN + Std
    models.append(imb_pipe(
        steps=[('t', StandardScaler()), ('e', SMOTEENN(enn=EditedNearestNeighbours(sampling_strategy='majority'))),
               ('m', LogisticRegression(solver='liblinear'))]))
    names.append('LR - Std - SE')

    # SMOTEENN + Power
    models.append(imb_pipe(steps=[('t1', MinMaxScaler()), ('t2', PowerTransformer()),
                                  ('e', SMOTEENN(enn=EditedNearestNeighbours(sampling_strategy='majority'))),
                                  ('m', LogisticRegression(solver='liblinear'))]))
    names.append('LR - Power - SE')

    return models, names, results


def get_models():
    # define models
    models, names, results = list(), list(), list()

    # Create pipelines of steps for LR and LDA
    # Use StandardScaler to apply on train and test data and then fit the model
    # LR
    models.append(Pipeline(steps=[('t', StandardScaler()), ('m', LogisticRegression(solver='liblinear'))]))
    names.append('LR')

    # LDA
    models.append(Pipeline(steps=[('t', StandardScaler()), ('m', LinearDiscriminantAnalysis())]))
    names.append('LDA')

    # NB
    models.append(GaussianNB())
    names.append('NB')

    return models, names, results


def eval_models(models, names, results, X, y):
    # evaluate each model
    for i in range(len(models)):
        # evaluate the model and store results
        scores = evaluate_model(X, y, models[i])
        results.append(scores)

        # summarize and store
        print('> %s %.3f (%.3f)' % (names[i], mean(scores), std(scores)))

    # plot the results
    plt.boxplot(results, showmeans=True)
    plt.xticks(list(range(1, len(names) + 1)), labels=names, rotation=45)

    plt.show()


def final_model(X, y):
    # define the model
    smoteenn = SMOTEENN(enn=EditedNearestNeighbours(sampling_strategy='majority'))
    model = LogisticRegression(solver='liblinear')
    pipeline = imb_pipe(steps=[('e', smoteenn), ('m', model)])

    # fit the model
    pipeline.fit(X, y)

    # evaluate on some non-spill cases (known class 0)
    print('Non-Spill Cases:')
    data = [[329, 1627.54, 1409.43, 51, 822500, 35, 6.1, 4610, 0.17, 178.4, 0.2, 0.24, 0.39, 0.12, 0.27, 138.32, 34.81,
             2.02, 0.14, 0.19, 75.26, 0.47, 351.67, 0.18, 9.24, 0.38, 2.57, -2.96, -0.28, 1.93, 0, 1.93, 34, 1710, 0,
             25.84, 78, 55, 1460.31, 710.63, 451.78, 150.85, 3.23, 0, 4530.75, 66.25, 7.85],
            [3234, 1091.56, 1357.96, 32, 8085000, 40.08, 8.98, 25450, 0.22, 317.7, 0.18, 0.2, 0.49, 0.09, 0.41, 114.69,
             41.87, 2.31, 0.15, 0.18, 75.26, 0.53, 351.67, 0.18, 9.24, 0.24, 3.56, -3.09, -0.31, 2.17, 0, 2.17, 281,
             14490, 0, 80.11, 78, 55, 4287.77, 3095.56, 1937.42, 773.69, 2.21, 0, 4927.51, 66.15, 7.24],
            [2339, 1537.68, 1633.02, 45, 5847500, 38.13, 9.29, 22110, 0.24, 264.5, 0.21, 0.26, 0.79, 0.08, 0.71, 89.49,
             32.23, 2.2, 0.17, 0.22, 75.26, 0.51, 351.67, 0.18, 9.24, 0.27, 4.21, -2.84, -0.29, 2.16, 0, 2.16, 228,
             12150, 0, 83.6, 78, 55, 3959.8, 2404.16, 1530.38, 659.67, 2.59, 0, 4732.04, 66.34, 7.67]]

    for row in data:
        # make prediction
        yhat = pipeline.predict([row])
        # get the label
        label = yhat[0]
        # summarize
        print('>Predicted=%d (expected 0)' % (label))

    # evaluate on some spill cases (known class 1)
    print('Spill Cases:')
    data = [[2971, 1020.91, 630.8, 59, 7427500, 32.76, 10.48, 17380, 0.32, 427.4, 0.22, 0.29, 0.5, 0.08, 0.42, 149.87,
             50.99, 1.89, 0.14, 0.18, 75.26, 0.44, 351.67, 0.18, 9.24, 2.5, 10.63, -3.07, -0.28, 2.18, 0, 2.18, 164,
             8730, 0, 40.67, 78, 55, 5650.88, 1749.29, 1245.07, 348.7, 4.54, 0, 25579.34, 65.78, 7.41],
            [3155, 1118.08, 469.39, 11, 7887500, 30.41, 7.99, 15880, 0.26, 496.7, 0.2, 0.26, 0.69, 0.11, 0.58, 118.11,
             43.96, 1.76, 0.15, 0.18, 75.26, 0.4, 351.67, 0.18, 9.24, 0.78, 8.68, -3.19, -0.33, 2.19, 0, 2.19, 150,
             8100, 0, 31.97, 78, 55, 3471.31, 3059.41, 2043.9, 477.23, 1.7, 0, 28172.07, 65.72, 7.58],
            [115, 1449.85, 608.43, 88, 287500, 40.42, 7.34, 3340, 0.18, 86.1, 0.21, 0.32, 0.5, 0.17, 0.34, 71.2, 16.73,
             1.82, 0.19, 0.29, 87.65, 0.46, 132.78, -0.01, 3.78, 0.7, 4.79, -3.36, -0.23, 1.95, 0, 1.95, 29, 1530,
             0.01, 38.8, 89, 69, 1400, 250, 150, 45.13, 9.33, 1, 31692.84, 65.81, 7.84]]

    for row in data:
        # make prediction
        yhat = pipeline.predict([row])
        # get the label
        label = yhat[0]
        # summarize
        print('>Predicted=%d (expected 1)' % (label))


def main():
    file_path = f"../data/oil_spill/oil-spill.csv"
    df = read_data(file_path)
    summarize_data(df, -1)
    plot_hist(df)

    X, y = load_dataset(file_path)
    dummy_classifier(X, y)

    models, names, results = get_models()
    # eval_models(models, names, results, X, y)

    m, n, r = get_improved_LR_models()
    models.extend(m)
    names.extend(n)
    results.extend(r)
    eval_models(models, names, results, X, y)

    final_model(X, y)


if __name__ == '__main__':
    main()
