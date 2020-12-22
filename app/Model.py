from app.view import *
import pickle
from tkinter import *


def edit_contact(edit_id: Entry):
    list_contact = load_database()
    edit_id_str = edit_id.get()
    for i in range(len(list_contact)):
        if edit_id_str == list_contact[i].id:
            new_edit_window, edit = create_record_window(2, edit_id_str)
            edit.name.insert(END, list_contact[i].name)
            edit.address.insert(END, list_contact[i].address)
            edit.phone.insert(END, list_contact[i].phone)
            edit.id.insert(END, list_contact[i].id)


def delete_contact(delete_id: Entry):
    list_contact = load_database()
    delete_id_str = delete_id.get()
    for i in range(len(list_contact)):
        if delete_id_str == list_contact[i].id:
            list_contact.pop(i)
            break
    with open("database.dat", "wb") as file:
        pickle.dump(list_contact, file)


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
