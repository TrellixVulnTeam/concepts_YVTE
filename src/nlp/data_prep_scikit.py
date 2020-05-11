from sklearn.feature_extraction.text import CountVectorizer
from nlp import data_prep_nltk  as data_prep


def model_count_vectorizer(list_docs):
    # text = ["The quick brown fox jumped over the lazy dog."]
    vectorizer = CountVectorizer()
    vectorizer.fit(list_docs)

    print(vectorizer.vocabulary_)
    vector = vectorizer.transform(list_docs)

    print(f"vector: {vector},\n"
          f"dtype: {type(vector)},\n"
          f"array: {vector.toarray()}")

    return vector


def load_text():
    filename = '../data/txts/metamorphosis_clean.txt'
    with open(filename, 'rt') as file:
        file = open(filename, 'rt')
        text = file.read()
    return text


def preprocess_initial():
    text = load_text()
    list_sentences = data_prep.splitting_into_words(text, splitter='sentences')
    model_count_vectorizer(list_sentences)


def main():
    preprocess_initial()
    pass


if __name__ == '__main__':
    main()
