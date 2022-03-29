import re
import pyperclip
from pymystem3 import Mystem
from datetime import datetime
import os

keyword_file = '/Volumes/big4photo/Documents/keywords/keywords in work.txt'

def notification(message):
    title = "Обработаны ключевые слова:"
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)

def bad_words_from_file():  # извлекаю слова исключения из текстового файла
    with open('bad_words.txt', 'r') as text_file:
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


def words_optimization(final=None):
    durty_words = pyperclip.paste().lower()
    bad_words = bad_words_from_file()
    optimization = re.findall(r'\w{3,}', durty_words)  # оставляю только слова длиннее трех букв
    optimization = (' '.join(optimization))
    lemmatized_words = "".join(Mystem().lemmatize(optimization))
    no_bad_words = re.sub(bad_words, '', lemmatized_words)  # удаляю слова паразиты
    final = re.sub(r'\b(\w+)(\s+\1)', r'\1', re.sub(r'\W+', ' ', no_bad_words),
                   flags=re.I).strip()  # удаляю повторы слов
    final = re.sub(r'\s+', ', ', final)  # разделяю слова запятыми

    write_keywords(final)
    pyperclip.copy(final)
    notification(final)
    print(final)


if __name__ == '__main__':
    words_optimization()
