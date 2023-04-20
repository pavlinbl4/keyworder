def bad_words_from_file(bad_word_file):  # извлекаю слова исключения из текстового файла
    with open(bad_word_file, 'r') as text_file:
        lines = text_file.readlines()
    bad_words = ''
    for i in lines:
        bad_words += '|' + i.strip()
    return f"\\b({bad_words.lstrip('|')})\\b"