# 1. Display window to the words that you want to optimise
from keyworder.text_input_window import create_input_window
from keyworder.words_more_two_litters import extract_words

if __name__ == '__main__':
    input_text = create_input_window()  # 1 get text from window
    durty_words = extract_words(input_text) #  2 create list with all words in text
    durty_words_set = set([word.lower() for word in durty_words]) #3 remove doubles and lowercase words
    # 4 lemma words in set
    # 5 remove bad words from set
