import tkinter as tk


def keyworder():  # оптимизация ключевых слов
    keywords = words.get()
    if keywords:
        from datetime import date
        import pyperclip
        txt = open('keywords in work.txt', 'a')
        date = str(date.today())

        bad_words = ['_РУССКИЙ_', ' и ', ' но ', ' в ', ' по ', ' за ']
        garbage = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '@',
                   '[',
                   '\\', ']', '^', '_', '`', '{', '|', '}', '~', '«', '»', '”', '-', ' ',
                   '“']  # список знаков препинания, которые нужно удалять

        for i in bad_words:  # заменяем ненужные слова пробелами
            keywords = keywords.replace(i, " ")

        for i in garbage:  # заменяем все знаки препинания на звездочку
            keywords = keywords.replace(i, "*")

        itog = set()
        double_dell = keywords.split("*")
        for i in double_dell:
            i = i.replace("*",
                          " ")  # в случае появления лишних звездочек заменяю их пробелами
            i = i.strip()
            if len(i) > 3 and i.isdigit() is False:  # удаляю слова меньше 4 букв и цифры
                itog.add(i.lower())  # добавляю слова в коллекцию, переводя их в нижний регистр

        keywords = sorted([i for i in itog])  # сортировка ключевых по алфавиту
        print(*keywords, sep=", ")

        pyperclip.copy(", ".join(keywords))  # передача результата в буфер обмена

        words.delete(0, tk.END)  # передача данных в окно программы
        words.insert(0, ", ".join(keywords))

        txt.write(date + '\n')  # запись ключевых слов в файл
        txt.write(", ".join(keywords) + '\n')
    else:
        error = tk.Label(win,
                         text="NO DATA",
                         fg='red'
                         )
        error.grid(row=5, column=5)


def clear_all():
    words.delete(0, tk.END)


win = tk.Tk()

# модуль отвечающий за вид окна программы
win.title("Keywords optimization")  # название окна
win.geometry("800x800+1600+300")  # размер окна
win.resizable(False, False)
win.config(bg="grey")  # цвет фона окна

# надпись над окном
label = tk.Label(win, text="INPUT keywords HERE",
                 bg="grey",
                 font=("Arial", 40,),
                 pady=30,  # отступ надписи сверху
                 )
label.place(x=180, y=1)

# окно для ввода информации
words = tk.Entry(win)
words.place(height=500, width=780, x=10, y=80)

# кнопка для выполнения действия
button = tk.Button(win,
                   text="OPTIMIZE",
                   command=keyworder,
                   pady=1  # отступ надписи сверху
                   )
button.place(x=400, y=700)

button_clear = tk.Button(win,
                         text="CLEAR",
                         command=clear_all
                         )
button_clear.place(x=400, y=600)

win.mainloop()  # цикл отвечающий за открытие окна
