import tkinter
import math
from tkinter import *

calculator = Tk()
inp = StringVar()
calculator.title("calculator")
calculator.geometry('435x490')


def create_button(row, column, text, command):
    button = Button(calculator, padx=16, pady=16, bd=8, font=('arial', 20, 'bold'), text=text, bg="orange",
                    command=command).grid(row=row, column=column)


entry = Entry(calculator, font=('arial', 26, 'bold'), bg="gray", textvariable=inp, bd=30, insertwidth=10,
          justify='right').grid(columnspan=30)

casle1 = create_button(1, 0, '1', lambda: casle1())
casle2 = create_button(1, 1, '2', lambda: casle2())
casle3 = create_button(1, 2, '3', lambda: casle3())
casle4 = create_button(2, 0, '4', lambda: casle4())
casle5 = create_button(2, 1, '5', lambda: casle5())
casle6 = create_button(2, 2, '6', lambda: casle6())
casle7 = create_button(3, 0, '7', lambda: casle7())
casle8 = create_button(3, 1, '8', lambda: casle8())
casle9 = create_button(3, 2, '9', lambda: casle9())
casle0 = create_button(4, 0, '0', lambda: casle0())
casleC = create_button(4, 1, 'c', lambda: clear())
equality = create_button(4, 2, '=', lambda: equality())
auditor = create_button(4, 5, ' . ', lambda: auditor())
plus = create_button(1, 4, ' +', lambda: plus())
minus = create_button(2, 4, ' - ', lambda: minus())
multiplied = create_button(3, 4, ' *', lambda: multiplied())
divided = create_button(4, 4, ' / ', lambda: divided())
caret = create_button(3, 5, '**', lambda: caret())
square_root = create_button(2, 5, '√', lambda: square_root())
percent = create_button(1, 5, '%', lambda: percent())


def casle1():
    casle1 = inp.get()
    inp.set(casle1 + '1')


def casle2():
    casle2 = inp.get()
    inp.set(casle2 + '2')


def casle3():
    casle3 = inp.get()
    inp.set(casle3 + '3')


def casle4():
    casle4 = inp.get()
    inp.set(casle4 + '4')


def casle5():
    casle5 = inp.get()
    inp.set(casle5 + '5')


def casle6():
    casle6 = inp.get()
    inp.set(casle6 + '6')


def casle7():
    casle7 = inp.get()
    inp.set(casle7 + '7')


def casle8():
    casle8 = inp.get()
    inp.set(casle8 + '8')


def casle9():
    casle9 = inp.get()
    inp.set(casle9 + '9')


def casle0():
    casle0 = inp.get()
    inp.set(casle0 + '0')


def plus():
    plus = inp.get()
    inp.set(plus + '+')


def minus():
    minus = inp.get()
    inp.set(minus + '-')


def multiplied():
    multiplied = inp.get()
    inp.set(multiplied + '*')


def divided():
    divided = inp.get()
    inp.set(divided + '/')


def caret():
    caret = inp.get()
    inp.set(caret + '**')


def auditor():
    auditor = inp.get()
    inp.set(auditor + '.')


def square_root():
    square_root = inp.get()
    result = math.sqrt(float(square_root))
    inp.set('√' + str(result))


def percent():
    percent = inp.get()
    inp.set(percent + '%')


def equality():
    equal = inp.get()
    inp.set(eval(equal))


def clear():
    inp.get()
    inp.set('')


calculator.mainloop()
