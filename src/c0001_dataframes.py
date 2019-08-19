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
    dict_a = {'col1': [10, 20, 30, 40, 50, 60],
              'col2': ['a', 'b', 'c', 'd', 'e', 'a'],
              'col3': ['!', '@', '#', '$', '%', '#']}
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


def sort_df(df, list_columns, list_bool_ascending):
    """
    Sort the DataFrame using list of columns provided.
    :param df:
    :param list_columns:
    :param list_bool_ascending:
    :return:

    """
    df.sort_values(by=list_columns, ascending=list_bool_ascending, inplace=True)

    # Other way
    df_tmp = df.sort_values(by=list_columns, ascending=list_bool_ascending)
    return df_tmp


def copy_df(df):
    """
    Copy a DataFrame and return a new reference to DataFrame having values same as the old one.
    :param df:
    :return:
    """

    # Useful to keep a copy of DataFrame to avoid any mis-references.
    df_tmp = df.copy()


def df_reset_index(df):
    """
    Code to reset the index i.e. row numbers
    :param df:
    :return:
    """
    # Don't assign to any variable because reset_index does not return the DataFrame.
    #  NoneType / AttributeError will be raised.
    df.reset_index(drop=True, inplace=True)
    return df


def invocations():
    # df1 = create_dataframe_from_dict_of_dict()
    # print_df(df1)
    pass


def main():
    """

    :return:
    """
    df = create_dataframe_from_dict()
    print_df(df)
    df = sort_df(df, ['col2', 'col1'], [False, True])
    print_df(df)
    df = df_reset_index(df)
    print_df(df)


if __name__ == '__main__':
    main()
