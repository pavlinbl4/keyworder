import re


def text_to_word_set(text):
    # Удаляем цифры и спецсимволы, оставляем только буквы, дефисы и пробелы
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s-]', '', text)

    # Преобразуем текст в строчный регистр и разделяем на слова
    words = cleaned_text.lower().split()

    # Удаляем слова короче трех букв и собираем уникальные слова в set
    word_set = {word for word in words if len(word) >= 3}

    return word_set

if __name__ == '__main__':

    text = "Пример текста с цифрами 123 и спецсимволами !@# пример текста."
    result = text_to_word_set(text)
    print(result)