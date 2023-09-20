# from tkinter import *
# root = Tk()
#
# # Creating a Label widget
# root.title('LIBRARY MANAGEMENT SYSTEM')
#
#
# def myClick():
#     mylabel = Label(root, text='Hello ' + input_box.get())
#     mylabel.grid(row=8, column=0)
#
#
# title = Label(root, text='NAMES')
# title2 = Label(root, text='ROLE')
# name1 = Label(root, text='1. NABASA ISAAC')
# name2 = Label(root, text='2. NINSIIMA AGGREY')
# name3 = Label(root, text='3. BUSINGYE HOPE')
# name4 = Label(root, text='4. YAWE ARTHUR')
# myButton = Button(root, text='NAMES', padx=50, pady=5, fg='indigo', bg='black')
# myButton1 = Button(root, text='Search', command=myClick, padx=50, pady=5, fg='white', bg='dark green')
# myButton2 = Button(root, text='About us', padx=50, pady=5, fg='white', bg='green')
# myButton3 = Button(root, text='Delete', padx=50, pady=5, fg='red', bg='green')
# input_box = Entry(root, width=20, bg='white', fg='red', borderwidth=2)
#
# # Showing widgets on the screen
# title.grid(row=0, column=0)
# title2.grid(row=0, column=1)
# name1.grid(row=1, column=0)
# name2.grid(row=2, column=0)
# name3.grid(row=3, column=0)
# name4.grid(row=4, column=0)
# myButton.grid(row=0, column=0)
# myButton1.grid(row=0, column=1)
# myButton2.grid(row=0, column=2)
# myButton3.grid(row=0, column=3)
# input_box.grid(row=1, column=1)
# input_box.insert(0, 'e.g XXXX@gmail.com')
#
# root.mainloop()

"""" The program below shows a simple calculator. Please enjoy it """

from tkinter import*
root = Tk()

# Building widgets
root.title('SIMPLE CALCULATOR')
insert_box = Entry(root, width=50)

myButton1 = Button(root, text='1')
myButton2 = Button(root, text='2')
myButton3 = Button(root, text='3')
myButton4 = Button(root, text='4')
myButton5 = Button(root, text='5')
myButton6 = Button(root, text='6')
myButton7 = Button(root, text='7')
myButton8 = Button(root, text='8')
myButton9 = Button(root, text='9')
myButton0 = Button(root, text='0')
myButton10 = Button(root, text='+')
myButton11 = Button(root, text='Clear')
myButton12 = Button(root, text='=')

# Showing widgets on the screen
insert_box.grid(row=0, column=0)
myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)
myButton9.grid(row=1, column=2)
myButton10.grid(row=4, column=0)
myButton11.grid(row=4, column=0)
myButton12.grid(row=4, column=0)
myButton1.grid(row=4, column=0)


root.mainloop()






















