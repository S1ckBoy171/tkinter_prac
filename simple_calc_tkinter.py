from tkinter import *

root = Tk()
root.title("simple calculator")
root.iconbitmap('c:/Users/samarthsachan/pictures/calculator.png')

e = Entry(root, width=40, borderwidth=7)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)


# for numbers
def click(numbers):
    new_number = e.get() + str(numbers)
    e.delete(0, END)
    e.insert(0, new_number)


# for clear
def clear():
    e.delete(0, END)
    return ()


#  functions
def add(first_number):
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)


def subtract(first_number):
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)


def division(first_number):
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def multiply(first_number):
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


# for equal
def Equal(second_number):
    num_1 = f_num
    if math == "add":
        e.delete(0, END)
        e.insert(0, int(num_1) + int(second_number))
    if math == "subtract":
        e.delete(0, END)
        e.insert(0, int(num_1) - int(second_number))
    if math == "multiply":
        e.delete(0, END)
        e.insert(0, int(num_1) * int(second_number))

    if math == "division":
        e.delete(0, END)
        e.insert(0, int(num_1) / int(second_number))


# define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: add(e.get()), bg="grey")
button_division = Button(root, text="/", padx=40, pady=20, command=lambda: division(e.get()), bg="grey")
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: multiply(e.get()), bg="grey")
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: subtract(e.get()), bg ="grey")
button_equal = Button(root, text="  =  ", padx=33, pady=20, command=lambda: Equal(e.get()), bg="light blue")
button_clear = Button(root, text="<Clr>", padx=29, pady=20, command=lambda: clear(), bg="red")

# display buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_division.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)

# main_loop

root.mainloop()
