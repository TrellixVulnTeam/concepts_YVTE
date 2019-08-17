"""
Code to understand how to use pandas DataFrames.
Audience: Beginners -> Advanced
@author: Shreedhar Kodate
"""
import pandas as pd


def print_df(df: pd.DataFrame) -> None:
    """
    Pretty print the basic DataFrame details.
    :param df:
    :return:
    """
    print(f"DataFrame: \n{df}")
    print(f"DataFrame Shape: \n{df.shape}")
    print(f"DataFrame Describe: \n{df.describe()}")
    print(f"DataFrame Columns: \n{df.columns}")
    print(f"DataFrame Index: \n{df.index}")


def create_dataframe_from_dict() -> pd.DataFrame:
    """
    Creates a dummy DataFrame from a basic python dictionary of lists.
    :return:
    """
    dict_a = {'col1': [10, 20, 30, 40, 50], 'col2': ['a', 'b', 'c', 'd', 'e'], 'col3': ['!', '@', '#', '$', '%']}
    df = pd.DataFrame(dict_a)
    return df


def create_dataframe_from_dict_of_dict() -> pd.DataFrame:
    """
    Creates a dummy DataFrame from a basic python dictionary of dictionaries.
    :return:
    """
    dict_b = {'col1': {'row1': 10, 'row2': 20, 'row3': 30, 'row4': 40, 'row5': 50},
              'col2': {'row1': 'a', 'row2': 'b', 'row3': 'c', 'row4': 'd', 'row5': 'e'},
              'col3': {'row1': '!', 'row2': '@', 'row3': '#', 'row4': '$', 'row5': '%'}}
    df = pd.DataFrame(dict_b)
    return df


def main():
    """

    :return:
    """
    df = create_dataframe_from_dict()
    print_df(df)
    df1 = create_dataframe_from_dict_of_dict()
    print_df(df1)


if __name__ == '__main__':
    main()
