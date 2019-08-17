import pandas as pd


def print_df(df):
    print(df)
    print(df.shape)
    print(df.describe())


def create_dataframe_from_dict():
    dict_a = {'col1': [10, 20, 30, 40, 50], 'col2': ['a', 'b', 'c', 'd', 'e'], 'col3': ['!', '@', '#', '$', '%']}
    df = pd.DataFrame(dict_a)
    return df


def create_dataframe_from_dict_of_dict():
    dict_b = {'col1': {'row1': 10, 'row2': 20, 'row3': 30, 'row4': 40, 'row5': 50},
              'col2': {'row1': 'a', 'row2': 'b', 'row3': 'c', 'row4': 'd', 'row5': 'e'},
              'col3': {'row1': '!', 'row2': '@', 'row3': '#', 'row4': '$', 'row5': '%'}}
    df = pd.DataFrame(dict_b)
    return df


def main():
    df = create_dataframe_from_dict()
    print_df(df)
    df1 = create_dataframe_from_dict_of_dict()
    print(df1)


if __name__ == '__main__':
    main()
