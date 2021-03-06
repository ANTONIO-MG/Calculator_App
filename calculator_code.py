from tkinter import *
import parser

root = Tk()
root.title('calculator')

#adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#get the user input and place it on the input field
i = 0
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def get_operator(operator):
    global i
    lenght = len(operator)
    display.insert()

def clear_all():
    display.delete(0, END)

def del_variables():
   display_string = display.get()
   if len(display_string):
       new_display_string = display_string[:-1]
       clear_all()
       display.insert(0, new_display_string)
   else:
       clear_all()
       display.insert(0, "Error")


#adding buttons to the calcuculator

Button(root, text="  1  ", command=lambda: get_variables(1)).grid(row=2, column=0)
Button(root, text="  2  ", command=lambda: get_variables(2)).grid(row=2, column=1)
Button(root, text="  3  ", command=lambda: get_variables(3)).grid(row=2, column=2)

Button(root, text="  4  ", command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="  5  ", command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="  6  ", command=lambda: get_variables(6)).grid(row=3, column=2)

Button(root, text="  7  ", command=lambda: get_variables(7)).grid(row=4, column=0)
Button(root, text="  8  ", command=lambda: get_variables(8)).grid(row=4, column=1)
Button(root, text="  9  ", command=lambda: get_variables(9)).grid(row=4, column=2)

#adding the additional buttons for the functions such as clear and additions and so on!

Button(root, text="  +  ").grid(row=2, column=3)
Button(root, text="  -  ").grid(row=3, column=3)
Button(root, text="  x  ").grid(row=4, column=3)
Button(root, text="  /  ").grid(row=5, column=3)

Button(root, text="  AC  ", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="  ,  ").grid(row=5, column=1)
Button(root, text="  0  ", command=lambda: get_variables(0)).grid(row=5, column=2)

#adding other operations to calculator

Button(root, text=" Del ", command=lambda: del_variables()).grid(row=2, column=4)
Button(root, text="  %  ").grid(row=3, column=4)
Button(root, text=" X! ").grid(row=4, column=4)
Button(root, text=" = ").grid(row=5, column=4)


# i just made an additional note here


root.mainloop()





