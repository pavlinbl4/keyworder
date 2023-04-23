import tkinter as tk


def create_checkbox_list(words,window_name):
    selected_words = []
    def submit():
        for i, word in enumerate(words):
            if checkboxes[i].get() == 1:
                selected_words.append(word)
        window.destroy()

    h = 30 * (len(words) % 10 + 10)
    l = 200 + 140 * ((len(words) // 10))
    window = tk.Tk()
    window.geometry(f"{l}x{h}")
    window.title(window_name)

    checkboxes = []
    for i, word in enumerate(words):
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=word.strip(), variable=var, onvalue=1, offvalue=0)
        checkbox.grid(row=i % 10, column=1 + i // 10, padx=30, pady=5, sticky='W')
        checkboxes.append(var)

    submit_button = tk.Button(window, text="Submit", command=submit)
    # submit_button.grid(row=i + 1, column=0, columnspan=len(words), padx=50, pady=5)
    submit_button.grid(row=i + 1, column=0, columnspan=len(words), pady=35)

    window.mainloop()
    return selected_words


# Example usage


# selected_words = []

if __name__ == '__main__':

    _words = create_checkbox_list(
        ["industrialisation", "apple", 'melon', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box', 'knife',
         'bread', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box', 'knife', 'bread', "industrialisation",
         "industrialisation", "apple", 'melon', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box', 'knife',
         'bread', 'fox', 'rabbit', 'box', 'knife', 'bread', 'fox', 'rabbit', 'box'])
    print(_words)
