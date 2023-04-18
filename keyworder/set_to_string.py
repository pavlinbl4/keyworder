def set_to_string(input_set):
    output_string = ", ".join(str(elem) for elem in input_set)
    return output_string


if __name__ == '__main__':
    print(set_to_string({'wolf', 'fox', 'donkey', 'rabbit'}))