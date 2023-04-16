import re


def remove_doubles(no_bad_words):
    return re.sub(r'\b(\w+)(\s+\1)', r'\1', re.sub(r'\W+', ' ', no_bad_words),
                  flags=re.I).strip()


def use_set(no_bad_words):
    return set(test_words.split(", "))


def re_remover_merlin(sentence):
    # Using regular expression to identify duplicate words
    return re.sub(r'\b(\w+)\b\s+\b\1\b', r'\1', sentence)


if __name__ == '__main__':
    test_words = "удаленный, работа, информационный, технология, хакер, взлом, хакинг, программа, киберпреступность, киберпреступник, кибермошенничество, киберпреступление, персональный, данные, мошенник, мошенничество, преступление, криминал, аноним, компьютер, монитор, интернет, телеком, информационный, технология, документ, электронный, документооборот, связь, телеком, социальный, сеть, человек, компьютер, переписка, общение, сервер, персональный, данные, оператор, информация, гаджет, занятость, карьера, компьютер, лаптоп, ноутбук, работа, технология, трудоустройство, удаленка, удаленный, работа, устройство, цифровизация"

    assert len(test_words) != len(remove_doubles(test_words))
    # print(len(test_words))
    print('list of input words')
    print(test_words.split(", "))
    print(len(test_words.split(", ")))
    print()

    print('remove doubles with regex')
    print(remove_doubles(test_words).split())
    print(len(remove_doubles(test_words).split()))
    print()

    print('remove doubles with set')
    print(use_set(test_words))
    print(len(use_set(test_words)))

    # print(re_remover_merlin(test_words).split(", "))
    # print(len(re_remover_merlin(test_words).split(", ")))
