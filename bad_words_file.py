import pyperclip

cgreen = '\33[0;32m'
cend = '\033[0m'
cred = '\033[91m'

def bad_words_from_file():
    with open('bad_words.txt', 'r') as text_file:
        lines = text_file.readlines()
    bad_words = ''
    for i in lines:
        bad_words += '|' + i.strip()
    bad_word_from_file = f"\\b({bad_words.lstrip('|')})\\b"
    print(bad_word_from_file)
    print(bad_words_old)
    print(bad_word_from_file == bad_words_old)

def add_bad_word():
    with open('bad_words.txt', 'a') as text_file:
        print(f"добавить слово {cred}{pyperclip.paste()}{cend}")
        text_file.write(pyperclip.paste()+'\n')


if __name__=='__main__':
    # bad_words_from_file()
    add_bad_word()