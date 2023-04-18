from pymystem3 import Mystem

from keyworder.words_more_two_litters import extract_words


def lema(any_text):
    lemmatized_words = extract_words(Mystem().lemmatize(any_text))
    return [word for word in lemmatized_words if len(word) > 2]


if __name__ == '__main__':
    print(lema(
        'Петербургское оборонное АО «Заслон» готовится разместить облигации на 1 млрд рублей, '
        'планируя за счет '
        'полученных средств финансировать расширение производственных площадок и '
        'модернизацию производств, '
        'а также направить деньги на софинансирование проектов гражданского назначения.'))
