# 1. Display window to the words that you want to optimise
import sys
import pyperclip
from loguru import logger

from Gui_keyworder_2023.gui_tools.new_input_window import create_input_window
from Gui_keyworder_2023.gui_tools.information_window import display_info
from Gui_keyworder_2023.gui_tools.checkbox_output import create_checkbox_list
from bad_words.bad_words_file import bad_words_from_file, write_bad_words_to_file
from Gui_keyworder_2023.save_data.check_file_exist import create_file_if_no
from Gui_keyworder_2023.save_data.write_keywords import write_keywords
from Gui_keyworder_2023.text_optimisation.lists_difference import list_dif

from Gui_keyworder_2023.text_optimisation.optimize_input_text import optimize_text

if __name__ == '__main__':
    path_to_keyword_file = create_file_if_no('keywords', 'keywords in work.txt')
    logger.info(path_to_keyword_file)
    path_to_bad_word_file = create_file_if_no('keywords', 'bad_words.txt')

    # 1 get text from window
    input_text = create_input_window("Enter text or keywords")
    logger.info(type(input_text))
    logger.info(input_text)

    # 2 get "bad words" from text file
    bad_words = bad_words_from_file(path_to_bad_word_file)
    logger.info(bad_words)

    dirty_words_set = optimize_text(input_text, bad_words)

    if len(dirty_words_set) > 0:

        dirty_words_list = [ word for word in dirty_words_set]

        # check keywords in GUI select words for work -> list off  selected words
        word_for_work = create_checkbox_list(dirty_words_list,
                                             window_name="Select keywords")

        # save words for work in text file
        write_keywords(",".join(word_for_work), path_to_keyword_file)
        print(f'{word_for_work = }')

        # now I want to check bad words
        unused_words = list_dif(dirty_words_set, word_for_work)
        pyperclip.copy(", ".join(word_for_work))
        print(f'{unused_words = }')

        selected_bad_words = create_checkbox_list(unused_words, window_name='select "Bad Words"')
        print(f'{selected_bad_words = }')

        write_bad_words_to_file(selected_bad_words, path_to_bad_word_file)  # copy words for work to clip memory

    else:
        print("NO KEYWORDS FOR WORK")
        display_info("NO KEYWORDS FOR WORK")
        sys.exit()

    display_info("WORK COMPLETE")
