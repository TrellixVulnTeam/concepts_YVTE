# Task 1: Import numpy package
import numpy as np


def numpy_version_and_config():
    # Task 2: Print numpy version and config
    print(f"Task 2: {np.__version__}, type: {type(np.__version__)}")
    np.show_config()


def np_commands():
    # Task 4: Command for getting info of add function
    # python - c "import numpy; numpy.info(numpy.add)"
    pass


def eval_expressions():
    # Task 15: What is the result of the following expression?
    exp1 = 0 * np.nan
    exp2 = np.nan == np.nan
    exp3 = np.inf > np.nan
    exp4 = np.nan - np.nan
    exp5 = 0.3 == 3 * 0.1
    print(f"Task 15: exp1: {exp1}, exp2: {exp2}, exp3: {exp3}, exp4: {exp4}, exp5: {exp5},")


def usage_arange():
    # Task 6: Create a vector with values ranging from 10 to 49
    # Hint: Last value is exclusive
    v = np.arange(10, 50)
    print(f"Task 6: {v}")

    # Task 7: Reverse a vector
    v = v[::-1]
    print(f"Task 7: {v}")


def operations_on_matrix():
    # Task 8: Create a 3x3 matrix with values ranging from 0 to 8
    mat = np.arange(9).reshape(3, 3)
    print("Task 8: ", mat)

    # Task 10: Create an identity matrix of size 3x3
    i_mat = np.eye(3)
    print(f"Task 10: {i_mat}")

    # Task 11: Create a 3x3x3 array with random values
    rand_mat = np.random.random((3, 3, 3))
    print(f"Task 11: {rand_mat}")

    # Task 12: Create a 2x2 array with random values and find the minimum and maximum values
    mat = np.random.random((2, 2))
    mat_min = mat.min()
    mat_max = mat.max()
    print(f"Task 12: mat: {mat} \n mat_min: {mat_min} mat_max: {mat_max}")

    # Task 14: Create a 2d array with 1 on the border and 0 inside
    mat = np.ones((5, 5))
    mat[1:-1, 1:-1] = 0
    print(f"Task 14: {mat}")


def operations_on_vector():
    # Task 3: Create a null vector of size 10
    null_vector = np.zeros(10)
    print(f"Task 3: {null_vector}")

    # Task 5: Set 5th value to 1
    null_vector[4] = 1
    print(f"Task 5: {null_vector}")

    # Task 9: Find indices of nonzero elements from [1,2,0,0,4,0]
    nz = np.nonzero([1, 2, 0, 0, 4, 0])
    print(f"Task 9: {nz}")

    # Task 13: Create a random vector of size 30 and find the mean value
    rand_vec = np.random.random(30)
    mean_val = rand_vec.mean()
    print(f"Task 13: rand_vec: {rand_vec} mean: {mean_val}")


def run_general():
    numpy_version_and_config()
    usage_arange()


def run_operations():
    operations_on_vector()
    operations_on_matrix()


def main():
    # Function calls to various independent concepts
    run_operations()
    eval_expressions()


if __name__ == '__main__':
    main()
