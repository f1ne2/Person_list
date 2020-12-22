from view import *
from Person import Person
from tkinter import *
import os


def find_contact(search_id_str: str, new_window: Tk, database: list):
    for i in range(len(database)):
        if search_id_str == database[i].id:
            output_find_contact(new_window, database, i)


def print_contacts(view_contacts_window: Tk, contacts_list: list):
    for i in range(len(contacts_list)):
        output_contact(view_contacts_window, contacts_list, i)


def save(new_contact_info: Person(Entry), i: int, contact_id: str):
    if os.path.exists("database.dat"):
        database = get_all_contacts()
        if i == 1:
            database.append(new_contact_info)
        if i == 2:
            for j in range(len(database)):
                if contact_id == database[j].id:
                    database.remove(database[j])
                    database.insert(j, new_contact_info)
                    break
    else:
        database = [new_contact_info]
    write_all_contacts(database)

