import re

from bad_words.bad_words_file import bad_words_from_file
from keyworder.lematization import lema
from keyworder.set_to_string import set_to_string
from keyworder.words_more_two_litters import extract_words
from kw_2023.check_file_exist import create_file_if_no


def optimize_text(input_text, bad_words):
    durty_words = extract_words(input_text)  # 2 create list with all words in text
    durty_words_string = set_to_string(durty_words)  # create string with all words
    durty_words_lema = lema(durty_words_string)  # lemmatize words and return list

    durty_words_set = set(durty_words_lema)  # convert to set and remove doubles

    durty_words_no_bad_words = re.sub(bad_words, '', set_to_string(durty_words_set))  # string

    return {word for word in durty_words_no_bad_words.split(', ') if len(word) > 2}


if __name__ == '__main__':
    bad_word_file = create_file_if_no('keywords', 'bad_words.txt')
    bad_words = bad_words_from_file(bad_word_file)
    input_text = 'На заседании Законодательного Собрания Санкт-Петербурга с ежегодным отчетом выступил начальникF Главного управления Министерства юстиции РФ по Санкт-Петербургу и Ленинградской области Сергей Феоктистов.'
    print(optimize_text(input_text, bad_words))
