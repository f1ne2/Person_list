from app.contact_review import *
from tkinter import *


def create_search_window():
    new_window = Tk()
    new_window.title("Welcome to Contacts list")
    new_window.geometry("500x250")

    lbl = Label(new_window, text="Options:", font=("Times New Roman", 16))
    lbl.grid(column=0, row=0)

    lbl = Label(new_window, text="ID:", font=("Times New Roman", 16))
    lbl.grid(column=1, row=1)

    search_id = Entry(new_window, width=20)
    search_id.grid(column=2, row=1)
    search_id.focus()

    btn = Button(new_window, text="Search ID", command=lambda:
    [get_id(search_id, new_window)])
    btn.grid(column=4, row=1)


def get_id(search_id: Entry, new_window: Tk):
    search_id_str = search_id.get()
    print_find_contact(search_id_str, new_window)


def print_find_contact(search_id_str: str, new_window: Tk):
    database = load_database()
    for i in range(len(database)):
        if search_id_str == database[i].id:
            lbl = Label(new_window,
                        text="Name: \t %s \t Address: "
                             "\t %s \t" "Phone: \t %s "
                             "\t ID:" "%s" %
                             (database[i].name,
                              database[i].address,
                              database[i].phone,
                              database[i].id),
                        font=("Times New Roman", 12))
            lbl.grid(column=0, row=i+4)