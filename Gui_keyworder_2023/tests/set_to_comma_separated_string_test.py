from unittest import TestCase, main

from Gui_keyworder_2023.text_optimisation.set_to_string import set_to_comma_separated_string


class SetToCommaString(TestCase):

    def test_empty_set(self):
        input_set = set()
        expected_output = ""
        self.assertEqual(set_to_comma_separated_string(input_set), expected_output)

    def test_output_type(self):
        input_set = {"apple", "banana", "cherry"}
        self.assertIsInstance(set_to_comma_separated_string(input_set), str)

    def test_invalid_input_type(self):
        invalid_input = [1, 2, 3]
        with self.assertRaises(TypeError):
            set_to_comma_separated_string(invalid_input)


if __name__ == '__main__':
    main()
