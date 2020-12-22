from app.Model import *
from app.Person import Person
from tkinter import *
import os


def print_find_contact(search_id_str: str, new_window: Tk):
    database = load_database()
    for i in range(len(database)):
        if search_id_str == database[i].id:
            lbl = Label(new_window, text="Name: \t %s \t Address: "
                                         "\t %s \t" "Phone: \t %s "
                                         "\t ID:" "%s" %
                                         (database[i].name,
                                          database[i].address,
                                          database[i].phone,
                                          database[i].id),
                        font=("Times New Roman", 12))
            lbl.grid(column=0, row=i+4)


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


def save(new_contact_info: Person(Entry), i: int, contact_id: str):
    if os.path.exists("database.dat"):
        with open("database.dat", "rb") as file:
            database = pickle.load(file)
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
    with open("database.dat", "wb") as file:
        pickle.dump(database, file)

