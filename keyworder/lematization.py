from pymystem3 import Mystem
from keyworder.words_more_two_litters import extract_words


def lema(any_text):
    lemmatized_words = extract_words(Mystem().lemmatize(any_text))
    return [word for word in lemmatized_words if len(word) > 2]


if __name__ == '__main__':
    print(lema(
        'крокодил крокодилов крокодилам Крокодилы crocodile'))
