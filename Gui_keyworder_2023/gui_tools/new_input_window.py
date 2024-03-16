"""only input window return tuple with list"""

import tkinter as tk

result_list = []


def create_input_window(window_name) -> tuple:
    def confirm_input():
        # get text input
        text = input_field.get("1.0", 'end-1c')
        result_list.append(text)
        window.destroy()

    def cancel_input():
        window.destroy()

    # Create window
    window = tk.Tk()
    window.title(window_name)

    # Set the height of the window to 100 pixels
    window_width = 570
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int(screen_width / 4)
    y = int(screen_height / 2 - window_height / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Disable the ability to resize the window
    window.resizable(False, False)

    # Text input field
    input_field = tk.Text(window)
    input_field.grid(row=0, column=0)

    # check button to torn on lematization

    def checkbutton_changed():
        if cbutton_rez.get() == 1:
            return 1
        else:
            return 0

    cbutton_rez = tk.IntVar()
    cb = tk.Checkbutton(window, text="Check for text lemmatization", variable=cbutton_rez)
    cb.grid(row=1, column=0, sticky="w", padx=150, pady=15)

    # Bind paste keyboard shortcut
    input_field.bind('<Control-v>', lambda e: input_field.event_generate('<<Paste>>'))

    # Bind enter key to confirm input
    input_field.bind('<Return>', confirm_input)

    # Paste button
    paste_btn = tk.Button(window, text="Paste", command=lambda: input_field.event_generate('<<Paste>>'))
    paste_btn.grid(row=2, column=0)

    # Other buttons
    tk.Button(window, text="Submit", command=lambda: [confirm_input(), checkbutton_changed()]).grid(row=3, column=0)
    tk.Button(window, text="Cancel", command=cancel_input).grid(row=4, column=0)

    window.mainloop()

    lemma_switch = checkbutton_changed()

    return result_list, lemma_switch


if __name__ == "__main__":
    print(create_input_window("This is window name"))
