# extract only words from string

import re


def extract_only_words_from_string(text_string) -> list:
    if isinstance(text_string, (list, tuple)):
        text_string = ' '.join(map(str, text_string))

    pattern = r'\b[-А-Яа-яA-Za-z]+\b'
    return re.findall(pattern, text_string)


if __name__ == '__main__':
    print(extract_only_words_from_string('Hello-World How-are-you?'))
