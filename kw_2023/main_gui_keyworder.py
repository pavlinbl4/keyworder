# 1. Display window to the words that you want to optimise
import sys
import pyperclip
from bad_words.bad_words_file import bad_words_from_file, add_bad_words_from_list
from gui_windows.output_window import display_info
from keyworder.checkbox_output import create_checkbox_list
from gui_windows.text_input_window import create_input_window
from keyworder.keyworder_2022_main import write_keywords
from kw_2023.check_file_exist import create_file_if_no
from kw_2023.lists_difference import list_dif
from kw_2023.optimize_input_text import optimize_text

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
        write_keywords(",".join(word_for_work))
        print(f'{word_for_work = }')

        # now I want to check bad words
        unused_words = list_dif(durty_words_set, word_for_work)
        pyperclip.copy(", ".join(word_for_work))
        print(f'{unused_words = }')

        selected_bad_words = create_checkbox_list(unused_words, window_name='select "Bad Words"')
        print(f'{selected_bad_words = }')

        add_bad_words_from_list(selected_bad_words, bad_word_file)  # copy words for work to clip memory

    else:
        print("NO KEYWORDS FOR WORK")
        display_info("NO KEYWORDS FOR WORK")
        sys.exit()

    display_info("WORK COMPLETE")
