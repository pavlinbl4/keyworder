# 1. Display window to the words that you want to optimise
from bad_words.bad_words_file import bad_words_from_file, add_bad_words_from_list
from confirm_window.output_window import display_info
from keyworder.check_file_exist import create_file_if_no
from keyworder.checkbox_output import create_checkbox_list
from keyworder.lists_difference import list_dif
from keyworder.optimize_input_text import optimize_text
from keyworder.text_input_window import create_input_window
from keyworder.write_keywords import write_keywords
import sys
import pyperclip

if __name__ == '__main__':
    keyword_file = create_file_if_no('keywords', 'keywords in work.txt')
    bad_word_file = create_file_if_no('keywords', 'bad_words.txt')

    input_text = create_input_window()  # 1 get text from window

    bad_words = bad_words_from_file(bad_word_file)

    durty_words_set = optimize_text(input_text, bad_words)

    if len(durty_words_set) > 0:

        # check keywords in GUI select words for work -> list off  selected words
        word_for_work = create_checkbox_list(durty_words_set,
                                             window_name="Select keywords")

        # save words for work in text file
        write_keywords(",".join(word_for_work), keyword_file)
        print(f'{word_for_work = }')

        # now I want to check bad words
        unused_words = list_dif(durty_words_set, word_for_work)
        pyperclip.copy(", ".join(unused_words))
        print(f'{unused_words = }')

        selected_bad_words = create_checkbox_list(unused_words, window_name='select "Bad Words"')
        print(f'{selected_bad_words = }')

        add_bad_words_from_list(selected_bad_words, bad_word_file)  # copy words for work to clip memory


    else:
        print("NO KEYWORDS FOR WORK")
        display_info("NO KEYWORDS FOR WORK")
        sys.exit()

    display_info("WORK COMPLETE")
