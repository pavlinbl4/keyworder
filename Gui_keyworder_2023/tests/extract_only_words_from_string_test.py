from unittest import TestCase, main

from Gui_keyworder_2023.text_optimisation.only_words_from_string import extract_only_words_from_string


class ExtractOnlyWords(TestCase):
    def test_int_input(self):
        int_input = 99
        with self.assertRaises(TypeError):
            extract_only_words_from_string(int_input)

    def test_multiple_words(self):
        text_string = "Hello World, How are you?"
        self.assertEqual(extract_only_words_from_string(text_string), ["Hello", "World", "How", "are", "you"])

    def test_words_with_hyphen(self):
        text_string = "Hello-World How-are-you?"
        self.assertEqual(extract_only_words_from_string(text_string), ['Hello-World', 'How-are-you'])

    def test_words_with_other_characters(self):
        text_string = "Hello, World! 123 @#$%^&*"
        self.assertEqual(extract_only_words_from_string(text_string), ["Hello", "World"])

    def test_list_input(self):
        text_string = ["Hello", " ", "World"]
        self.assertEqual(extract_only_words_from_string(text_string), ["Hello", "World"])

    def test_empty_string(self):
        text_string = ""
        self.assertEqual(extract_only_words_from_string(text_string), [])

if __name__ == '__main__':
    main()
