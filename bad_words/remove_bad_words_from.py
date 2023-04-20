import re

from bad_words.bad_words_file import bad_words_from_file
from keyworder.check_file_exist import create_file_if_no


def bad_words_remover(durty_words_string):
    bad_word_file = create_file_if_no('keywords', 'bad_words.txt')
    bad_words = bad_words_from_file(bad_word_file)
    return re.sub(bad_words, "", durty_words_string)


if __name__ == '__main__':
    print(bad_words_remover(" 'также', 'олень', 'тюдень', 'также'"))
