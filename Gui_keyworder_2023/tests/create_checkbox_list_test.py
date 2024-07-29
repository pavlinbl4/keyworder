from Gui_keyworder_2023.gui_tools.checkbox_output import create_checkbox_list
from unittest import TestCase, main
from unittest.mock import MagicMock
import tkinter as tk


class TestCreateCheckboxList(TestCase):
    def setUp(self):
        self.words = ["apple", "banana", "cherry", "date", "elderberry"]
        self.window_name = "Test Window"

    def test_create_checkbox_list(self):
        # Mocking Tkinter window
        tk.Tk = MagicMock()

        # Mocking Tkinter methods
        tk_instance = tk.Tk()
        tk_instance.winfo_screenwidth = MagicMock(return_value=800)
        tk_instance.winfo_screenheight = MagicMock(return_value=600)
        tk_instance.geometry = MagicMock()

        # Calling the function
        result = create_checkbox_list(self.words, self.window_name)

        # Check if Tkinter methods were called properly
        tk_instance.title.assert_called_once_with(self.window_name)
        tk_instance.geometry.assert_called_once_with("800x400+200+100")
        self.assertEqual(tk_instance.mainloop.call_count, 0)

        # Assertions for the result
        self.assertEqual(result, [])


if __name__ == "__main__":
    main()
