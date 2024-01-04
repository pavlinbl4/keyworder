import re


def no_doubles(no_bad_words):  # возвращает строку со словами разделенными пробелами
    re_cleaner = re.sub(r'\b(\w+)(\s+\1)', r'\1', re.sub(r'\W+', ' ', no_bad_words),
                        flags=re.I).strip()
    return ", ".join(sorted([i for i in set(re_cleaner.split(' '))]))


if __name__ == '__main__':
    print(no_doubles('слон, слон, dog, fox, dog'))

    assert no_doubles('слон, слон, dog, fox, dog') == 'dog, fox, слон'
    assert no_doubles('слон, слон, пес') == 'пес, слон'