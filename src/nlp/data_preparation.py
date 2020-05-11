import string
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def nltk_prep_2(list_words):
    # Generally used Porter Stemmer algorithm: https://tartarus.org/martin/PorterStemmer/
    porter_stem = PorterStemmer()
    word_stem = [porter_stem.stem(word) for word in list_words]

    # Always review the word tokens after doing any operation on textual data - Jason Brownlee
    print(word_stem[:100])
    return word_stem


def nltk_prep_1(text):
    # Data preparation using nltk: http://www.nltk.org/book/ch03.html
    # Splits the long text into words
    word_tokens = word_tokenize(text)
    word_lower = [word.lower() for word in word_tokens]
    re_remove_punctuation = re.compile('[%s]' % re.escape(string.punctuation))
    word_removed_punctuation = [re_remove_punctuation.sub('', word) for word in word_lower]
    # Remove non alphabetic words
    word_alpha = [word for word in word_removed_punctuation if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    word_removed_stopwords = [word for word in word_alpha if word not in stop_words]

    print(word_removed_stopwords[:100])
    return word_removed_stopwords


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
    lower = kwargs.get('lower', True)
    re_expression = kwargs.get('re_expression', r'\W+')

    if splitter == 're':
        list_words = re.split(re_expression, text)
    elif splitter == 'whitespaces':
        list_words = text.split()
    else:
        # Return sentences
        list_words = text.replace('\n', ' ').split('.')

    if lower:
        list_words = [word.lower() for word in list_words]

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
    # list_words = splitting_into_words(text, splitter='')
    list_words = remove_punctuation_from_words(list_words)
    list_words = remove_non_printable_from_words(list_words)
    print(list_words[:100])


def main():
    preprocess_initial()
    pass


if __name__ == '__main__':
    main()
