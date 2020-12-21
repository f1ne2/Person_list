from app.delete_contact import *
from app.edit_contact import *
from tkinter import *


def create_view_window():
    viewing_window = Tk()
    viewing_window.title("Contacts list review")
    viewing_window.geometry("750x250")
    lbl = Label(viewing_window, text="Contacts:",
                font=("Times New Roman", 16))
    lbl.grid(column=0, row=0)
    del_butn(viewing_window)
    edit_butn(viewing_window)
    print_contacts(viewing_window)


def print_contacts(view_contacts_window: Tk):
    contacts_list = load_database()
    for i in range(len(contacts_list)):
        lbl = Label(view_contacts_window, text="Name: \t %s \t Address: "
                                               "\t %s \t" "Phone: \t %s "
                                               "\t ID:" "%s" %
                                               (contacts_list[i].name,
                                                contacts_list[i].address,
                                                contacts_list[i].phone,
                                                contacts_list[i].id),
                    font=("Times New Roman", 12))
        lbl.grid(column=0, row=i+2)


def load_database():
    list_contacts = []
    file = open("database.dat", "rb")
    while 1:
        try:
            list_contacts = pickle.load(file)
        except EOFError:
            break
    file.close()
    return list_contacts


def del_butn(view_contacts_window: Tk):
    btn = Button(view_contacts_window, text="Delete contact",
                 command=create_delete_window)
    btn.grid(column=3, row=0)


def edit_butn(view_contacts_window: Tk):
    btn = Button(view_contacts_window, text="Edit contact",
                 command=create_edit_window)
    btn.grid(column=4, row=0)


