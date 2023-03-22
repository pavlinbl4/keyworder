import re
import pyperclip
from pymystem3 import Mystem
from datetime import datetime
from notific import notification
from pathlib import Path
import os
from check_file_exist import create_file_if_no

path_to_folder = f'{Path().home()}/Documents/keywords'
os.makedirs(path_to_folder, exist_ok=True)
keyword_file = create_file_if_no(path_to_folder, 'keywords in work.txt')
bad_word_file = create_file_if_no(path_to_folder, 'bad_words.txt')


def bad_words_from_file():  # извлекаю слова исключения из текстового файла
    with open(bad_word_file, 'r') as text_file:
        lines = text_file.readlines()
    bad_words = ''
    for i in lines:
        bad_words += '|' + i.strip()
    return f"\\b({bad_words.lstrip('|')})\\b"


def write_keywords(final):
    with open(keyword_file, 'a') as text_file:
        text_file.write('\n')
        text_file.write(datetime.now().strftime("%Y-%m-%d") + '\n')
        text_file.write(final)


def remove_doubles(no_bad_words):
    # return re.sub(r'\b(\w+)(\s+\1)', r'\1', re.sub(r'\W+', ' ', no_bad_words),
    #               flags=re.I).strip()  # удаляю повторы слов
    return ", ".join([word.strip() for word in set(no_bad_words) if word.isprintable()])



def words_optimization():
    durty_words = pyperclip.paste().lower()  # 1 keyword for optimisation from clip - string
    # bad_words = bad_words_from_file()  # keywords from file that I want to delete
    bad_words = 'черепаха'
    optimization = re.findall(r'\w{3,}', durty_words)  # words longer 3 letters - list
    optimization = (', '.join(optimization))  # list to string
    # lemmatized_words = "".join(Mystem().lemmatize(optimization))  # string
    lemmatized_words = Mystem().lemmatize(optimization)  # list after lema
    no_doubles = remove_doubles(lemmatized_words)  # remove doubles
    final = re.sub(bad_words, '', no_doubles)  # удаляю слова паразиты



    # final = re.sub(r'\s+', ', ', no_doubles)  # разделяю слова запятыми

    write_keywords(final)
    pyperclip.copy(final)
    notification(final, 'Обработаны ключевые слова:')
    return final


if __name__ == '__main__':
    words_optimization()
    # assert words_optimization() is not None
    # assert type(words_optimization()) == str
