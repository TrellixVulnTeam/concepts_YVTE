import re


def splitting_into_words(text, **kwargs):
    words = []
    splitter = kwargs.get('splitter', 're')
    re_expression = kwargs.get('re_expression', r'\W+')

    if splitter == 're':
        words = re.split(re_expression, text)
    elif splitter == 'whitespaces':
        words = text.split()
    else:
        words = text.split('.')

    return words


def load_text():
    filename = '../data/txts/metamorphosis_clean.txt'
    with open(filename, 'rt') as file:
        file = open(filename, 'rt')
        text = file.read()
    return text


def preprocess_initial():
    text = load_text()
    words = splitting_into_words(text)
    words = splitting_into_words(text, splitter='whitespaces')
    print(words[:100])


def main():
    preprocess_initial()
    pass


if __name__ == '__main__':
    main()
