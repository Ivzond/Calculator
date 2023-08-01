import math
from tkinter import *
from tkinter import ttk

# Создание основного окна
root = Tk()
root.title('Калькулятор')
root.geometry('300x400')


# Создание поля ввода
entry = Entry(root, width=40, bd=5)
entry.grid(row=0, column=0, columnspan=4)


# Функция для добавления символов в поле ввода
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


# Функция для обработки всех операций
def button_operation(operation):
    try:
        if operation == "ln":
            result = math.log(float(entry.get()))
        else:
            current = entry.get()
            entry.delete(0, END)
            entry.insert(0, str(current) + operation)
            return
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Ошибка")


# Функция, подсчитывающая результат
def button_equal_click():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, 'Ошибка')


# Функция, очищающая поле ввода
def button_clear_click():
    entry.delete(0, END)


# Назначения кнопок цифр
button_1 = ttk.Button(root, text='1', command=lambda: button_click(1))
button_2 = ttk.Button(root, text='2', command=lambda: button_click(2))
button_3 = ttk.Button(root, text='3', command=lambda: button_click(3))
button_4 = ttk.Button(root, text='4', command=lambda: button_click(4))
button_5 = ttk.Button(root, text='5', command=lambda: button_click(5))
button_6 = ttk.Button(root, text='6', command=lambda: button_click(6))
button_7 = ttk.Button(root, text='7', command=lambda: button_click(7))
button_8 = ttk.Button(root, text='8', command=lambda: button_click(8))
button_9 = ttk.Button(root, text='9', command=lambda: button_click(9))
button_0 = ttk.Button(root, text='0', command=lambda: button_click(0))

# Расположение кнопок с цифрами
button_1.grid(row=3, column=0, ipadx=10, ipady=10)
button_2.grid(row=3, column=1, ipadx=10, ipady=10)
button_3.grid(row=3, column=2, ipadx=10, ipady=10)
button_4.grid(row=4, column=0, ipadx=10, ipady=10)
button_5.grid(row=4, column=1, ipadx=10, ipady=10)
button_6.grid(row=4, column=2, ipadx=10, ipady=10)
button_7.grid(row=5, column=0, ipadx=10, ipady=10)
button_8.grid(row=5, column=1, ipadx=10, ipady=10)
button_9.grid(row=5, column=2, ipadx=10, ipady=10)
button_0.grid(row=6, column=1, ipadx=10, ipady=10)

# Назначение кнопок с операциями
button_plus = ttk.Button(root, text='+', command=lambda: button_operation('+'))
button_minus = ttk.Button(root, text='-', command=lambda: button_operation('-'))
button_multiplication = ttk.Button(root, text='x', command=lambda: button_operation('*'))
button_division = ttk.Button(root, text='/', command=lambda: button_operation('/'))
button_parentheses_1 = ttk.Button(root, text='(', command=lambda: button_operation('('))
button_parentheses_2 = ttk.Button(root, text=')', command=lambda: button_operation(')'))
button_power = ttk.Button(root, text='^', command=lambda: button_operation('**'))
button_ln = ttk.Button(root, text='ln', command=lambda: button_operation('ln'))
button_equal = ttk.Button(root, text='=', command=lambda: button_equal_click())
button_clear = ttk.Button(root, text='clear', command=lambda: button_clear_click())

# Расположение кнопок с операциями
button_plus.grid(row=7, column=0, ipadx=10, ipady=10)
button_minus.grid(row=7, column=1, ipadx=10, ipady=10)
button_multiplication.grid(row=8, column=0, ipadx=10, ipady=10)
button_division.grid(row=8, column=1, ipadx=10, ipady=10)
button_parentheses_1.grid(row=7, column=2, ipadx=10, ipady=10)
button_parentheses_2.grid(row=8, column=2, ipadx=10, ipady=10)
button_power.grid(row=9, column=0, ipadx=10, ipady=10)
button_ln.grid(row=6, column=0, ipadx=10, ipady=10)
button_equal.grid(row=9, column=1, ipadx=10, ipady=10)
button_clear.grid(row=9, column=2, ipadx=10, ipady=10)

# Запуск окна с программой
root.mainloop()
