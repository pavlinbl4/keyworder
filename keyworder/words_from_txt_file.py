from keyworder.words_more_tree_litters import extract_words


def words_from_file(txt_file):
    with open(txt_file, 'r') as text_file:
        lines = text_file.readlines()
    words = ''
    for i in lines:
        if i.strip().isprintable():
            words += i.strip()
    # bad_word_from_file = f"\\b({words.lstrip('|')})\\b"
    # print(bad_word_from_file)
    return extract_words(lines)


if __name__ == '__main__':
    print(words_from_file('/Users/evgeniy/Documents/keywords/keywords in work.txt'))
