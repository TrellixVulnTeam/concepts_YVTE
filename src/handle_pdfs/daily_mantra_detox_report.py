"""
Installation instructions
sudo apt-get install python3
pip install beautifulsoup4 lxml

https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup

"""
import argparse
import datetime as dtime
import math
import pandas as pd
from bs4 import BeautifulSoup


def mine_html(params):
    """
    style="border:1px solid #eaeaea" width="100%"

    @return:
    """
    with open(params['html_path'], 'r') as fh:
        str_html = fh.read()

    soup = BeautifulSoup(str_html, "lxml")
    get_table(soup, params['table_style'])


def get_name(cell):
    p_tag = cell.find('p')

    mobile_number = p_tag.contents[0].contents[0]
    name = p_tag.contents[1]

    str_value = f"{mobile_number}{name}"
    return {'name': name.replace('-', '').strip(), 'mobile_number': mobile_number}


def get_time(cell):
    p_tag = cell.find('p')
    str_value = f"{p_tag.contents[0]}"
    return str_value


def get_start_time(cell):
    return {'start_time': get_time(cell)}


def get_end_time(cell):
    return {'end_time': get_time(cell)}


def get_total_minutes(cell):
    return {'total_minutes': int(get_time(cell).replace('m', ''))}


def get_value(cell, cell_type):
    dict_response = {
        'name': get_name,
        'start_time': get_start_time,
        'end_time': get_end_time,
        'total_minutes': get_total_minutes
    }
    return dict_response[cell_type](cell)


def get_rounds(x_mins):
    return math.floor(x_mins / 7.5)


def get_whatsapp_msg(df_table):
    names_rounds = '\n'.join([f"{row['name']} {row['rounds']}" for index, row in df_table.iterrows()])
    total_holy_names = df_table['rounds'].sum() * 108 * 16
    msg = f"Hare Krishna devotees,\n\n" \
          f"Śrī Śrī Radha Krishnachandra ki jai! \n" \
          f"Śrī Śrī Krishna Balaram ki jai! \n" \
          f"Śrī Śrī Nitai Gauranga ki jai! \n\n" \
          f"Jagadguru Srila Prabhupāda ki jai!\n\n" \
          f"Today we chanted {total_holy_names} holy names of Lord.\n\n" \
          f"\n{names_rounds}\n\n\n" \
          f"Venue: Over phone call\n" \
          f"Timings: 7:30-9:30 AM\n\n" \
          f"Request others to join us tomorrow🙏🏻."

    print(''.join(['-'] * 50))
    print(msg)
    print(''.join(['-'] * 50))
    return msg


def get_image_msg(df_table):
    total_holy_names = df_table['rounds'].sum()
    msg = f"Today we collectively served " \
          f"Lord Sri Radha Krishnachandra's lotusfeet " \
          f"by chanting [{total_holy_names}] rounds " \
          f"of Hare Krishna Mahamantra." \
          f"\n" \
          f"{len(df_table['name'])} devotees participated."
    print(''.join(['-'] * 50))
    print(msg)
    print(''.join(['-'] * 50))
    return msg


def get_table(soup, table_style, **kwargs):
    tables = soup.find_all('table', attrs={'style': table_style})

    for index, table in enumerate(tables):
        rows = table.tbody.find_all("tr")  # contains 2 rows
        # print(f"rows: {rows}")

        list_rows = []
        for row_index, row in enumerate(rows):
            # print(f"row_index: {row_index}")
            cells = row.find_all('td')
            # for cell_index, cell in enumerate(cells):
            #     if cell_index in [0, 5, 6, 7]:
            #         print(f"cell: {cell_index}: {cell}")
            if len(cells) >= 8:
                dict_row = {}

                dict_row.update(get_value(cells[0], 'name'))
                dict_row.update(get_value(cells[5], 'start_time'))
                dict_row.update(get_value(cells[6], 'end_time'))
                dict_row.update(get_value(cells[7], 'total_minutes'))

                list_rows.append(dict_row)

        df_table = pd.DataFrame(list_rows)
        df_table['rounds'] = df_table['total_minutes'].apply(get_rounds)
        # print(f"df_table: {index}\n{df_table}")

        str_ts = dtime.datetime.now().strftime("%Y_%m_%d")
        df_table.to_csv(f"report_{str_ts}.csv", index=False)

        get_whatsapp_msg(df_table)
        get_image_msg(df_table)


def setup():
    pd.options.display.max_rows = 999
    pd.set_option('max_colwidth', 40)
    pd.set_option('max_rows', 5)
    pd.set_option('expand_frame_repr', True)
    pd.options.display.max_colwidth = 100


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--html_path', help='Pass file path', type=str, default='./data/conf_report.html')
    parser.add_argument('-style', '--table_style', help='Table tag style', type=str, default="border:1px solid #eaeaea")
    parsed_args, _ = parser.parse_known_args()
    x = parsed_args.html_path
    dict_args = vars(parsed_args)
    return dict_args


def main():
    """
    Command to run:
    python daily_mantra_detox_report.py -f data/conf_report.html
    python daily_mantra_detox_report.py -f ../../../../../Downloads/tmp_conf.html
    @return:
    """
    params = parse_args()
    mine_html(params)


if __name__ == '__main__':
    main()
