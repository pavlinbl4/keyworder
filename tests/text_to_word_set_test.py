from unittest import TestCase, main

from text_optimisation.text_optimisation import text_to_word_set


class ExtractOnlyWords(TestCase):
    def test_int_input(self):
        int_input = 99
        with self.assertRaises(TypeError):
            text_to_word_set(int_input)

    def test_multiple_words(self):
        text_string = "Hello World, How are you?"
        self.assertEqual(text_to_word_set(text_string), {"hello", "world", "how", "are", "you"})

    def test_words_with_hyphen(self):
        text_string = "Hello-World How-are-you?"
        self.assertEqual(text_to_word_set(text_string), {'how-are-you', 'hello-world'})

    def test_words_with_other_characters(self):
        text_string = "Hello, World! 123 @#$%^&*"
        self.assertEqual(text_to_word_set(text_string), {"hello", "world"})

    def test_list_input(self):
        text_string = '"Hello", " ", "World"'
        self.assertEqual(text_to_word_set(text_string), {"hello", "world"})

    def test_empty_string(self):
        text_string = ""
        self.assertEqual(text_to_word_set(text_string), set())

if __name__ == '__main__':
    main()
