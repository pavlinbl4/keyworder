from unittest import TestCase, main

from Gui_keyworder_2023.text_optimisation.remove_doubles import no_doubles


class NoDoubleWords(TestCase):
    def test_one_word_tree_times(self):
        input_string = 'fox,   fox   fox'
        self.assertTrue(no_doubles(input_string), 'fox')

    def test_string(self):
        input_string = '    rabbit,слон, слон, dog, fox, dog, rabbit'
        self.assertTrue(no_doubles(input_string), 'dog, fox, rabbit, слон')



if __name__ == '__main__':
    main()