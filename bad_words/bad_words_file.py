"""
this function add word from clip memory to the file with "bad" words
"""

import pyperclip
from pathlib import Path
import os
from keyworder.check_file_exist import create_file_if_no

from colorama import Fore
from confirm_window.confirm_word import confirmation_window
from keyworder.notific import notification


def bad_words_from_file(file_path):
    with open(file_path, 'r') as text_file:
        lines = text_file.readlines()
    bad_words = ''
    for i in lines:
        bad_words += '|' + i.strip()
    bad_word_from_file = f"\\b({bad_words.lstrip('|')})\\b"  # I don't remember why I create this f - stroke
    # print(bad_word_from_file)
    return bad_word_from_file


def add_bad_word():
    with open(bad_word_file, 'a') as text_file:
        new_bad_word = pyperclip.paste()
        if new_bad_word in bad_words_from_file(bad_word_file):
            print(f'{Fore.GREEN}{new_bad_word}{Fore.RESET}\n'
                  f'уже сожержится в списке исключений')
        else:
            if confirmation_window(new_bad_word):
                notification(new_bad_word, 'Добавлено исключение')
                print(f"слово\n{Fore.RED}{new_bad_word}{Fore.RESET}\n"
                      f"добавлено в список исключений")
                text_file.write(new_bad_word + '\n')

def add_bad_words_from_list(list, bad_word_file):
    with open(bad_word_file, 'a') as text_file:
        for word in list:
            if word not in bad_words_from_file(bad_word_file):
                text_file.write(word + '\n')



if __name__ == '__main__':
    path_to_folder = f'{Path().home()}/Documents/keywords'
    os.makedirs(path_to_folder, exist_ok=True)
    bad_word_file = create_file_if_no(path_to_folder, 'bad_words.txt')
    add_bad_word()
