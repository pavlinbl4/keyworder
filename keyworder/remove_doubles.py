import re


def no_doubles(no_bad_words):  # возвращает строку со словами разделенными пробелами
    re_cleaner = re.sub(r'\b(\w+)(\s+\1)', r'\1', re.sub(r'\W+', ' ', no_bad_words),
                        flags=re.I).strip()
    return ", ".join([i for i in set(re_cleaner.split(' '))])


if __name__ == '__main__':
    print(no_doubles(
        'коммерческий, недвижимость, свая, строительство, стройка,   парраы стройплощадка, коммерческий, недвижимость, свая, строительство, стройка, стройплощадка'))
