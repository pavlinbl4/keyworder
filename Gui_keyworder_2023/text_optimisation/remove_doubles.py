import re


# возвращает строку со словами разделенными запятой, убирая повторы
def no_doubles(no_bad_words):
    re_cleaner = re.sub(r'\b(\w+)(\s+\1)', r'\1', re.sub(r'\W+', ' ', no_bad_words),
                        flags=re.I).strip()
    return ", ".join(sorted([i for i in set(re_cleaner.split(' '))]))


