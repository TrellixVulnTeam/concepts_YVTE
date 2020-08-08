"""
Installation instructions
sudo apt-get install python3
pip install pypdf2 pandas
pip install pdfminer.six
pip install requests beautifulsoup4 lxml

"""
import sys
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
    print(soup.prettify())  # print the parsed data of html


def main():
    path = '/home/shreedhar/Downloads/tmp_conf_call_report.pdf'
    mine_text(path)


if __name__ == '__main__':
    main()
