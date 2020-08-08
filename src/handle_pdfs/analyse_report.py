"""
Installation instructions
sudo apt-get install python3
pip install pypdf2 pandas
pip install pdfminer.six
pip install requests beautifulsoup4 lxml

https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup

"""
import datetime as dtime
import math
import sys
import pandas as pd
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text, extract_text_to_fp
from bs4 import BeautifulSoup
import requests


def print_info(pdf_path, information, number_of_pages):
    txt = f"""
        Information about {pdf_path}: 

        Author: {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages: {number_of_pages}
        """

    print(txt)
    return information


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        print_info(pdf_path, information, number_of_pages)

        for page in range(number_of_pages):
            obj_page = pdf.getPage(page)
            text = obj_page.extractText()
            print(f"page: {page}\n{text}")


def mine_text(pdf_path):
    # with open('samples/simple1.pdf', 'rb') as fin:
    #     extract_text_to_fp(fin, output_string)
    # print(output_string.getvalue().strip())

    # text = extract_text(pdf_path)
    # print(repr(text))
    # print(text)

    if sys.version_info > (3, 0):
        from io import StringIO
    else:
        from io import BytesIO as StringIO
    from pdfminer.layout import LAParams
    output_string = StringIO()
    with open(pdf_path, 'rb') as fin:
        extract_text_to_fp(fin,
                           output_string,
                           laparams=LAParams(),
                           output_type='html',
                           codec=None)
    str_html = output_string.getvalue().strip()
    with open('temp.html', 'w') as fh:
        fh.write(str_html)

    # url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    #
    # # Make a GET request to fetch the raw HTML content
    # html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(str_html, "lxml")
    # print(soup.prettify())  # print the parsed data of html


def get_links(soup):
    print(soup.title)
    print(soup.title.text)

    list_links = []
    for link in soup.find_all("a"):
        dict_link = {
            'inner_text': link.text,
            'title': link.get("title"),
            'href': link.get("href")
        }
        list_links.append(dict_link)
    print(f"list_links: {list_links}")
    return list_links


def mine_html(html_path):
    """
    style="border:1px solid #eaeaea" width="100%"

    @param html_path:
    @return:
    """
    with open(html_path, 'r') as fh:
        str_html = fh.read()

    # url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    #
    # # Make a GET request to fetch the raw HTML content
    # html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(str_html, "lxml")
    # print(soup.prettify())  # print the parsed data of html

    get_links(soup)
    get_table(soup, '')


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


def get_table(soup, table_class, **kwargs):
    # tables = soup.find("table", attrs={"class": table_class})

    tables = soup.find_all('table', attrs={'style': "border:1px solid #eaeaea"})

    for index, table in enumerate(tables):
        rows = table.tbody.find_all("tr")  # contains 2 rows
        # print(f"rows: {rows}")

        list_rows = []
        for row_index, row in enumerate(rows):
            print(f"row_index: {row_index}")
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
        print(f"df_table: {index}\n{df_table}")

        str_ts = dtime.datetime.now().strftime("%Y_%m_%d")
        df_table.to_csv(f"report_{str_ts}.csv", index=False)

        get_whatsapp_msg(df_table)
        get_image_msg(df_table)

    # tables = soup.find_all("table")
    #
    # for index, table in enumerate(tables):
    #     rows = table.tbody.find_all("tr")  # contains 2 rows
    #
    #     # Get all the headings of Lists
    #     headings = []
    #     for td in rows[0].find_all("td"):
    #         # remove any newlines and extra spaces from left and right
    #         cell = td.b
    #         if cell is not None:
    #             headings.append(cell.text.replace('\n', ' ').strip())
    #
    #     print(f"index: {index}, \nheadings: {headings}")


def setup():
    pd.options.display.max_rows = 999
    pd.set_option('max_colwidth', 40)
    pd.set_option('max_rows', 5)
    pd.set_option('expand_frame_repr', True)
    pd.options.display.max_colwidth = 100


def main():
    path = '/home/shreedhar/Downloads/tmp_conf_call_report.pdf'
    html_path = '/home/shreedhar/Downloads/tmp_conf.html'
    # mine_text(path)
    mine_html(html_path)


if __name__ == '__main__':
    main()
