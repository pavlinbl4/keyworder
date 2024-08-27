from unittest import TestCase, main

from text_optimisation.set_to_string import set_to_comma_separated_string


class SetToCommaString(TestCase):

    def test_empty_set(self):
        input_set = set()
        expected_output = ""
        self.assertEqual(set_to_comma_separated_string(input_set), expected_output)

    def test_output_type(self):
        input_set = {"apple", "banana", "cherry"}
        self.assertIsInstance(set_to_comma_separated_string(input_set), str)

    def test_wrong_output_type(self):
        input = ["apple", "banana", "cherry"]
        with self.assertRaises(TypeError):
            set_to_comma_separated_string(input)


if __name__ == '__main__':
    main()
