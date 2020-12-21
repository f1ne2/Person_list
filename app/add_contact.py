from app.edit_contact import *
from app.Person import *
from tkinter import *
import pickle
import os
from tkinter import messagebox


def create_record_window(i: int, contact_id: str) -> Tk and \
                                                           Person(Entry):
    info = Person()
    new_window = Tk()
    new_window.title("Welcome to Contacts list")
    new_window.geometry("1000x250")

    lbl = Label(new_window, text="Options:", font=("Times New Roman", 16))
    lbl.grid(column=0, row=0)

    lbl = Label(new_window, text="Name:", font=("Times New Roman", 16))
    lbl.grid(column=1, row=1)

    lbl = Label(new_window, text="Address:", font=("Times New Roman", 16))
    lbl.grid(column=3, row=1)

    lbl = Label(new_window, text="Phone:", font=("Times New Roman", 16))
    lbl.grid(column=5, row=1)

    lbl = Label(new_window, text="ID:", font=("Times New Roman", 16))
    lbl.grid(column=7, row=1)

    info.name = Entry(new_window, width=20)
    info.name.grid(column=2, row=1)
    info.name.focus()

    info.address = Entry(new_window, width=20)
    info.address.grid(column=4, row=1)

    info.phone = Entry(new_window, width=20)
    info.phone.grid(column=6, row=1)

    info.id = Entry(new_window, width=20)
    info.id.grid(column=8, row=1)
    if i == 1:
        confirm_add_button(new_window, info, 1)
    if i == 2:
        confirm_edit_button(new_window, info, 2, contact_id)
    return new_window, info


def confirm_add_button(new_window: Tk, info: Person(Entry), i: int):
    btn = Button(new_window, text="Confirm", command=lambda:
    (show_message(), get_text(info, i, "0"), new_window.destroy()))
    btn.grid(column=9, row=1)


def show_message():
    messagebox.showinfo(title="Information", message="Successful")


def get_text(info: Person(Entry), i: int, contact_id: str):
    new_contact_info = Person()
    new_contact_info.name = info.name.get()
    new_contact_info.address = info.address.get()
    new_contact_info.phone = info.phone.get()
    new_contact_info.id = info.id.get()
    save(new_contact_info, i, contact_id)


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

