"""
A program that stores this book information:

Client name, carrier, Status, last reach out

User can:

View all records
Search an entry
Add an entry
Update entry
Delete Close
"""

from tkinter import *
import tkinter.messagebox
from datetime import date
import backend, reminders

today = date.today()
date_text = today.strftime("%m/%d/%y")
window = Tk()

window.wm_title("EDI Files")


def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        clear_command()
        e1.insert(END,selected_tuple[1])
        e2.insert(END,selected_tuple[2])
        e3.insert(END,selected_tuple[3])
        l5.config(text=selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)


def clear_command():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')


def search_command():
    list1.delete(0, END)
    for row in backend.search(client_text.get(), carrier_text.get(), status_text.get()):
        list1.insert(END, row)
    clear_command()


def add_command():
    backend.insert(client_text.get(), carrier_text.get(), status_text.get(), date_text)
    clear_command()
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def update_command():
    try:
        backend.update(selected_tuple[0],client_text.get(), carrier_text.get(), status_text.get(), date_text)
    except IndexError:
        pass
    clear_command()
    view_command()


def show_files_need_update():
    files = reminders.get_info()
    list1.delete(0,END)
    for file in files:
        list1.insert(END, file)


l1 = Label(window, text="Client")
l1.grid(row=0, column=0)

l2 = Label(window, text="Carrier")
l2.grid(row=0, column=2)

l3 = Label(window, text="Status")
l3.grid(row=1, column=0)

l4 = Label(window, text="Date")
l4.grid(row=1, column=2)

client_text = StringVar()
e1 = Entry(window, textvariable = client_text)
e1.grid(row=0, column=1)

carrier_text = StringVar()
e2 = Entry(window, textvariable = carrier_text)
e2.grid(row=0, column=3)

status_text = StringVar()
e3 = Entry(window, textvariable = status_text)
e3.grid(row=1, column=1)


l5 = Label(window, text=date_text)
l5.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Follow up files", width=12, command=show_files_need_update)
b2.grid(row=3, column=3)

b3 = Button(window, text="Search entry", width=12, command=search_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Add entry", width=12, command=add_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Update", width=12, command=update_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Delete", width=12, command=delete_command)
b6.grid(row=7, column=3)


view_command()
window.mainloop()


