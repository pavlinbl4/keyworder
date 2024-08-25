import re
import pyperclip
from datetime import datetime
from keyworder.lematization import lema
from keyworder.notific import notification
from kw_2023.check_file_exist import create_file_if_no
from pathlib import Path
import os

path_to_folder = f'{Path().home()}/Documents/keywords'
os.makedirs(path_to_folder, exist_ok=True)
keyword_file = create_file_if_no(path_to_folder, 'keywords in work.txt')
bad_word_file = create_file_if_no(path_to_folder, 'bad_words.txt')


def bad_words_from_file(path_to_bad_word_file: str):  # извлекаю слова исключения из текстового файла
    with open(path_to_bad_word_file, 'r') as text_file:
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
    return ", ".join([word.strip() for word in set(no_bad_words) if word.isprintable()])


def words_optimization():
    dirty_words = pyperclip.paste().lower()  # 1 keyword for optimisation from clip - string

    bad_words = 'черепаха'
    optimization = re.findall(r'\w{3,}', dirty_words)  # words longer 3 letters - list
    optimization = (','.join(optimization))  # list to string
    # lemmatized_words = "".join(Mystem().lemmatize(optimization))  # string
    lemmatized_words = lema(optimization)  # list after lema
    no_doubles = remove_doubles(lemmatized_words)  # remove doubles
    final = re.sub(bad_words, '', no_doubles)  # удаляю слова паразиты

    write_keywords(final)
    pyperclip.copy(final)
    notification(final, 'Обработаны ключевые слова:')
    return final


if __name__ == '__main__':
    words_optimization()
    assert words_optimization() is not None
    assert type(words_optimization()) == str
