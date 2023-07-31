import tkinter as tk
from tkinter import font


def display_info(info):
    root = tk.Tk()
    root.title("Information Window")

    # Set window size
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int(screen_width / 4)
    y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Set font
    custom_font = font.Font(family="Didot", size=24)

    # Add label with specified font and color
    label = tk.Label(root, text=info, font=custom_font, fg="yellow")
    label.pack(pady=20)

    # Add close button
    button = tk.Button(root, text="Close", command=root.destroy)
    button.pack(pady=40)

    # Start the main loop
    root.mainloop()

if __name__ == '__main__':
    display_info("NO KEYWORDS FOR WORK")
