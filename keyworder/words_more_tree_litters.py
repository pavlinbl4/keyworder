"""
function receive list or srting with words  and symbols and return only words
"""

import re


def extract_words(text_string):
    if type(text_string) is list:
        text_string = ''.join(text_string)
    pattern = r'[А-Яа-яA-Za-z]+\-*[А-Яа-яA-Za-z]+'
    return re.findall(pattern, text_string)


if __name__ == '__main__':
    print(
        extract_words(
            'beautifulsoup42023-03-22конюшенный,, 2023,, petersburg,, ,, saint,, пассажир, wi-fi, канал,, инвентарь'))
    # print(extract_words(['\n', '2023-03-15\n', '\n', 'Крысы не дают покоя полосатым кошкам\n']))
