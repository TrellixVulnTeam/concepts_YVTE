import pandas as pd


def print_df(df):
    print(df)
    print(df.shape)
    print(df.describe())


def create_dataframe_from_dict():
    dict_a = {'col1': [10, 20, 30, 40, 50], 'col2': ['a', 'b', 'c', 'd', 'e'], 'col3': ['!', '@', '#', '$', '%']}
    df = pd.DataFrame(dict_a)
    return df


def main():
    df = create_dataframe_from_dict()
    print_df(df)


if __name__ == '__main__':
    main()
