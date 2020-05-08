import string
import re


def remove_non_printable_from_words(list_words):
    re_print = re.compile("[^%s]" % re.escape(string.printable))
    list_printable = [re_print.sub('', w) for w in list_words]
    return list_printable


def remove_punctuation_from_words(list_words):
    print(f'removing: {string.punctuation}')
    # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    list_stripped = [re_punc.sub('', w) for w in list_words]
    return list_stripped


def splitting_into_words(text, **kwargs):
    list_words = []
    splitter = kwargs.get('splitter', 're')
    re_expression = kwargs.get('re_expression', r'\W+')

    if splitter == 're':
        list_words = re.split(re_expression, text)
    elif splitter == 'whitespaces':
        list_words = text.split()
    else:
        # Return sentences
        list_words = text.replace('\n', ' ').split('.')

    return list_words


def load_text():
    filename = '../data/txts/metamorphosis_clean.txt'
    with open(filename, 'rt') as file:
        file = open(filename, 'rt')
        text = file.read()
    return text


def preprocess_initial():
    text = load_text()
    list_words = splitting_into_words(text)
    list_words = splitting_into_words(text, splitter='')
    list_words = remove_punctuation_from_words(list_words)
    list_words = remove_non_printable_from_words(list_words)
    print(list_words[:100])


def main():
    preprocess_initial()
    pass


if __name__ == '__main__':
    main()
