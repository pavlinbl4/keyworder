def list_dif(list1, list2):
    return [x for x in list1 if x not in list2]


if __name__ == '__main__':
    print(list_dif([1, 2, 3, 4, 5], [5, 1]))
