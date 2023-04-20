from datetime import datetime

def write_keywords(final, keyword_file):
    with open(keyword_file, 'a') as text_file:
        text_file.write('\n')
        text_file.write(datetime.now().strftime("%Y-%m-%d") + '\n')
        text_file.write(final)