from app.Search_contact import *
from app.contact_review import *
from app.add_contact import *
from tkinter import *


def button_add(window: Tk):
    btn1 = Button(window, text="Add new contact",
                  command=lambda: (create_record_window(1, "0")))
    btn1.grid(column=0, row=1)


def button_search(window: Tk):
    btn4 = Button(window, text="Search contact",
                  command=create_search_window)
    btn4.grid(column=0, row=2)


def button_view(window: Tk):
    btn5 = Button(window, text="View contact list",
                  command=create_view_window)
    btn5.grid(column=0, row=3)


def button_exit(window: Tk):
    btn6 = Button(window, text="Exit", command=window.quit)
    btn6.grid(column=0, row=4)


def main_screen():
    window = Tk()
    window.title("Welcome to Contacts list")
    lbl = Label(window, text="Options:", font=("Times New Roman", 16))
    lbl.grid(column=0, row=0)
    window.geometry("500x250")
    return window