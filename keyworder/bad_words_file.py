import pyperclip
from notific import notification
from colorama import Fore


def bad_words_from_file():
    with open('bad_words.txt', 'r') as text_file:
        lines = text_file.readlines()
    bad_words = ''
    for i in lines:
        bad_words += '|' + i.strip()
    bad_word_from_file = f"\\b({bad_words.lstrip('|')})\\b"
    # print(bad_word_from_file)
    return lines


def add_bad_word():
    with open('bad_words.txt', 'a') as text_file:
        new_bad_word = pyperclip.paste()
        if new_bad_word in bad_words_from_file():
            notification(new_bad_word, 'Добавлено исключение')
            print(f"слово\n{Fore.RED}{new_bad_word}{Fore.RESET}\n"
                  f"добавлено в список исключений")
            text_file.write(new_bad_word + '\n')
        else:
            print(f'{Fore.GREEN}{new_bad_word}{Fore.RESET}\n'
                  f'уже сожержится в списке исключений')


if __name__ == '__main__':
    # print(bad_words_from_file())
    add_bad_word()
