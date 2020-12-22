from Person import Person
import pickle
from tkinter import *


def edit_contact(edit_id_str: str, edit: Person):
    list_contact = get_all_contacts()
    for i in range(len(list_contact)):
        if edit_id_str == list_contact[i].id:
            edit.name.insert(END, list_contact[i].name)
            edit.address.insert(END, list_contact[i].address)
            edit.phone.insert(END, list_contact[i].phone)
            edit.id.insert(END, list_contact[i].id)


def delete_contact(delete_id: Entry):
    list_contact = get_all_contacts()
    delete_id_str = delete_id.get()
    for i in range(len(list_contact)):
        if delete_id_str == list_contact[i].id:
            list_contact.pop(i)
            break
    with open("database.dat", "wb") as file:
        pickle.dump(list_contact, file)


def get_all_contacts() -> list:
    list_contacts = []
    file = open("database.dat", "rb")
    while 1:
        try:
            list_contacts = pickle.load(file)
        except EOFError:
            break
    file.close()
    return list_contacts


def write_all_contacts(database: list):
    with open("database.dat", "wb") as file:
        pickle.dump(database, file)

