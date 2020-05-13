from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nlp import data_prep_nltk  as data_prep


def model_tfidf_vectorizer(list_docs):
    list_docs = ["The quick brown fox jumped over the lazy dog.",
                 "The dev shree",
                 "The fox"]

    vectorizer = TfidfVectorizer()
    vectorizer.fit(list_docs)

    print(vectorizer.vocabulary_)
    print(vectorizer.idf_)

    for text in list_docs:
        vector = vectorizer.transform([text])
        print(vector.shape, vector.toarray())


def model_count_vectorizer(list_docs):
    # list_docs = ["The quick brown fox jumped over the lazy dog."]
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
    return list_sentences


def main():
    list_docs = preprocess_initial()
    # model_count_vectorizer(list_docs)
    model_tfidf_vectorizer(list_docs)
    pass


if __name__ == '__main__':
    main()
