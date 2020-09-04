# Machine Learning General Notes

## Contents
1. [Types of Machine Learning](#types-of-machine-learning)

### Types of Machine Learning
Reference: [MLM blog](https://machinelearningmastery.com/types-of-learning-in-machine-learning/)
1. Learning Problems
    1. Supervised
        1. Training: A mapping function from input vectors to output vectors
        2. Prediction: Take input vectors and produce output vectors
        3. Types:
            1. Classification (C): Predict a class(categorical) as output. E.g. MNIST handwritten digits
            2. Regression (R): Predict a numerical value(class) as output. E.g. House prices
        4. Popular Algorithms
            1. Decision Trees (C, R) 
            2. Linear Regression (R)
            3. Logistic Regression (C)
            4. SVM - Support Vector Machines (C, R)
            5. Artificial Neural Networks (C, R)
    2. Unsupervised
        1. Training: Extract relationships or patterns from input data without targets
        2. Types:
            1. Clustering: Finding groups in data.
            2. Density Estimation (DE): Summarizing the distribution of data.
            3. Visualization: Plotting data
            4. Projection: creating lower-dimensional representations of data.
        3. Popular Algorithms:    
            1. k-means
            2. Kernel DE
            3. PCA(Principal Component Analysis): summarizing a dataset in terms of eigenvalues and eigenvectors, 
                with linear dependencies removed
    3. Reinforcement 
2. Hybrid Learning problems
    1. Semi-Supervised
    2. Self-Supervised
    3. Multi-Instance 
3. Statistical Learning
    1. Inductive
    2. Deductive
    3. Transductive
4. Learning techniques
    1. Multi-task
    2. Active
    3. Online
    4. Transfer
    5. Ensemble