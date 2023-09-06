from keyworder.words_more_two_litters import extract_words


def words_from_file(txt_file:str):
    # read text file and return only words from it
    with open(txt_file, 'r') as text_file:
        lines = text_file.readlines()
    words = ''
    for i in lines:
        if i.strip().isprintable():
            words += i.strip()
    return extract_words(words)


if __name__ == '__main__':
    print(words_from_file('/Users/evgeniy/Documents/keywords/keywords in work.txt'))
