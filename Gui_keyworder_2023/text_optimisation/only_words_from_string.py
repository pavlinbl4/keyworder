# extract only words from string

import re


def extract_only_words_from_string(text_string):
    if type(text_string) is list:
        text_string = ''.join(text_string)
    pattern = r'[А-Яа-яA-Za-z]+\-*[А-Яа-яA-Za-z]+'
    return re.findall(pattern, text_string)



