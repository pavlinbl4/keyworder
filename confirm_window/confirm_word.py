"""
that receive string
and generate confirmation window with two
buttons "accept" and "decline" and return result
"""
import tkinter as tk


def confirmation_window(bad_word):
    answer = []
    root = tk.Tk()
    root.geometry("300x100")
    root.resizable(False, False)
    root.title("")

    message = tk.Label(root, text=f"Do you want to add word\n\n \"{bad_word}\"?")
    message.pack()

    def callback(value):
        root.destroy()
        if value == "Yes":
            answer.append(bad_word)

        return answer

        # return line if value == "Yes" else False

    yes_button = tk.Button(root, text="Yes", command=lambda: callback("Yes"))
    no_button = tk.Button(root, text="No", command=lambda: callback("No"))
    yes_button.pack(side=tk.LEFT, padx=30)
    no_button.pack(side=tk.RIGHT, padx=30)

    # Run the window
    root.mainloop()

    # if len(answer)
    return True if len(answer) == 1 else False


if __name__ == '__main__':
    print(confirmation_window('fox'))
