import os
import sys
import subprocess
import string
import pyperclip
from random import choice
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('300x300')
root.title('Password Generator')
root.resizable(0, 0)
root.iconbitmap(os.getcwd()+r'\assets\img\icon.ico')
root.configure(bg='#121212')


# Functions
letters_ascii = list(string.ascii_letters + string.digits + '!@#$%^&*')
def GeneratePassword():
    # global lenght_entry
    # global result_entry
    global password
    result_entry.delete(0, END)
    if len(lenght_entry.get()) > 4:
        messagebox.showerror(title='Problem with numbers', message='Please enter the numbers correctly and must be between 1 and 4 digits\n( {} ) => The length of letters is more than 4'.format(lenght_entry.get()))

    else:
        try:
            range_of_input = int(lenght_entry.get())

            password = ''

            for i in range(0, range_of_input):
                password += choice(letters_ascii)

            result_entry.config(state=NORMAL)

            result_entry.insert(0, password)

            # result_entry.config(state=DISABLED)

            copy_btn.config(state=NORMAL)

        except ValueError:
            messagebox.showerror(title='Problem with numbers',
                                 message='Please insert a number and must be between 1 and 4 digits\n\n( {} ) => not found in numbers'.format(lenght_entry.get()))


def copy():
    pyperclip.copy(password)

def developer():
    messagebox.showinfo('About Developer', 'Hello, I am Amir Hossein Ghanmi.\n I designed this program and the good thing about this program is that when you register on a site, the site asks you for a password, you can create it with this program.')
lenght_label = Label(root, text='Enter Password Lenght',bg='#121212', fg='white', font=('arial', 12))
lenght_entry = Entry(root, width=25, borderwidth=2, font=('arial', 12))

genbutton = Button(root, text='Generate Password', bg='#121212', fg='white',
                    borderwidth=3, padx=50, command=GeneratePassword)

result_label = Label(root, text='Generated Password',bg='#121212', fg='white', font=('arial', 12))
result_entry = Entry(root, width=25, borderwidth=2, font=('arial', 12))

copy_btn = Button(root, text='Copy Generated Password', bg='#121212', fg='white',
                   borderwidth=3, padx=50, state=DISABLED, command=copy)
# Load Widgets

lenght_label.place(relx=0.5, rely=0.05, anchor='c')
lenght_entry.place(relx=0.5, rely=0.15, anchor='c')
genbutton.place(relx=0.5, rely=0.30, anchor='c')
result_label.place(relx=0.5, rely=0.4, anchor='c')
result_entry.place(relx=0.5, rely=0.5, anchor='c')
copy_btn.place(relx=0.5, rely=0.65, anchor='c')


root.mainloop()
