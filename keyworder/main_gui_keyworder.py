# 1. Display window to the words that you want to optimise
from bad_words.bad_words_file import bad_words_from_file, add_bad_words_from_list
from keyworder.check_file_exist import create_file_if_no
from keyworder.checkbox_output import create_checkbox_list
from keyworder.lematization import lema
from keyworder.lists_difference import list_dif
from keyworder.set_to_string import set_to_string
from keyworder.text_input_window import create_input_window
from keyworder.words_more_two_litters import extract_words
from keyworder.write_keywords import write_keywords
import re

if __name__ == '__main__':
    keyword_file = create_file_if_no('keywords', 'keywords in work.txt')
    bad_word_file = create_file_if_no('keywords', 'bad_words.txt')

    input_text = create_input_window()  # 1 get text from window

    durty_words = extract_words(input_text)  # 2 create list with all words in text
    durty_words_string = set_to_string(durty_words)

    #  remove bad words
    bad_words = bad_words_from_file(bad_word_file)
    durty_words_set = re.sub(bad_words, '', durty_words_string)
    durty_words_lema = lema(durty_words_string)  # make string for lema
    durty_words_set = set(durty_words_lema)  # remove double words

    # check keywords in GUI
    word_for_work = create_checkbox_list(durty_words_set,
                                         window_name="Select keywords")  # select words for work -> list off  selected words

    # save words for work in text file
    write_keywords(",".join(word_for_work), keyword_file)
    print(f'{word_for_work = }')

    # now I want to check bad words
    unused_words = list_dif(durty_words_set, word_for_work)
    print(f'{unused_words = }')

    selected_bad_words = create_checkbox_list(unused_words, window_name='select "Bad Words"')
    print(f'{selected_bad_words = }')

    add_bad_words_from_list(selected_bad_words, bad_word_file)

    # copy words for work to clip memory

    # find not selected words and display this words to add some of tman to bad words
