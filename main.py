from tkinter import *

root = Tk()
root.title('A calculator by anukul')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)


def button_click(number):
    current = e.get()
    e.delete(0, END)

    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    global sign
    sign = '+'
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    global sign
    sign = '-'
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    global sign
    sign = '/'
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    global sign
    sign = '*'
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    if sign == '+':
        e.delete(0, END)

        e.insert(0, int(f_num) + int(second_number))

    if sign == '-':
        e.delete(0, END)

        e.insert(0, int(f_num) - int(second_number))
    if sign == '*':
        e.delete(0, END)

        e.insert(0, int(f_num) * int(second_number))
    if sign == '/':
        e.delete(0, END)

        e.insert(0, float(f_num) / float(second_number))


button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1),fg='red')
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2),fg='red')
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3),fg='red')
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4),fg='red')
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5),fg='red')
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6),fg='red')
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7),fg='red')
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8),fg='red')
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9),fg='red')
button_10 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0),fg='red')
button_clear = Button(root, text='AC', padx=35, pady=20, command=button_clear, bg='red', fg='black')
button_add = Button(root, text='+', padx=40, pady=20, command=button_add,fg='red')
button_sub = Button(root, text='-', padx=40, pady=20, command=button_sub,fg='red')
button_div = Button(root, text='/', padx=40, pady=20, command=button_div,fg='red')
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply,fg='red')
button_equal = Button(root, text='=', padx=140, pady=20, command=button_equal, bg='blue', fg='white')

# put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_10.grid(row=4, column=0)
button_clear.grid(row=4, column=2)
button_add.grid(row=4, column=1)
button_sub.grid(row=5, column=0)
button_div.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)

button_equal.grid(row=6, column=0, columnspan=3)

root.mainloop()
