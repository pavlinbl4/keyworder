import re


def extract_only_words(text_string: str) -> list:
    # function takes a string, extracts words composed of letters and optional hyphens/asterisks
    # and returns a list of those extracted words
    if type(text_string) is list:
        text_string = ''.join(text_string)
    # pattern = r'[А-Яа-яA-Za-z]+\-*[А-Яа-яA-Za-z]+'   #  Cyrillic or Latin letters
    pattern = r'[А-Яа-я]+\-*[А-Яа-я]+'  # only words in Cyrillic
    return re.findall(pattern, text_string)

def no_doubles(no_bad_words):  # возвращает строку со словами разделенными пробелами
    re_cleaner = re.sub(r'\b(\w+)(\s+\1)', r'\1', re.sub(r'\W+', ' ', no_bad_words),
                        flags=re.I).strip()
    return ", ".join([i for i in set(re_cleaner.split(' '))])


def words_from_file(txt_file:str):
    # read text file and return only words from it
    with open(txt_file, 'r') as text_file:
        lines = text_file.readlines()
    words = ''
    for i in lines:
        if i.strip().isprintable():
            words += i.strip()
    return extract_only_words(words)


if __name__ == '__main__':
    print(words_from_file('/Users/evgeniy/Documents/keywords/keywords in work.txt'))
