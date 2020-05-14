from keras_preprocessing.text import text_to_word_sequence, one_hot, hashing_trick


def prep_1(text):
    text = "The quick brown fox jumped over the lazy dog."

    list_unique_words = list(set(text_to_word_sequence(text)))
    print(f"docs: {list_unique_words[:100]}")

    vocab_size = len(list_unique_words)
    print(f"vocab_size: {vocab_size}")

    oh_encoding = one_hot(text, n=round(vocab_size * 1.3))
    print(f"oh_encoding: {oh_encoding}")

    hashed_doc = hashing_trick(text, n=round(vocab_size * 1.3), hash_function='md5')
    print(f"hashed_doc: {hashed_doc}")

    return oh_encoding


def main():
    prep_1("")


if __name__ == '__main__':
    main()
