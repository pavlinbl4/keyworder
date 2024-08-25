import tkinter as tk
from tkinter import font

from gui_windows.geometry import set_window_size


def display_info(info):
    window = tk.Tk()
    window.title("Information Window")

    # Set window size

    set_window_size(window, window_height=200, window_width=400)

    # Set font
    custom_font = font.Font(family="Didot", size=24)

    # Add label with specified font and color
    label = tk.Label(window, text=info, font=custom_font, fg="yellow")
    label.pack(pady=20)

    # Add close button
    button = tk.Button(window, text="Close", command=window.destroy)
    button.pack(pady=40)

    # Start the main loop
    window.mainloop()


if __name__ == '__main__':
    display_info("NO KEYWORDS FOR WORK")
