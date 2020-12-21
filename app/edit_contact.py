from app.contact_review import *
from app.add_contact import *
from app.Person import *
from tkinter import *


def create_edit_window():
    edit_window = Tk()
    edit_window.title("Welcome to Contacts list")
    edit_window.geometry("500x250")
    lbl = Label(edit_window, text="If you want to edit contact,"
                                  "enter contact's ID and press Edit",
                font=("Times New Roman", 12))
    lbl.grid(column=0, row=0)
    edit_id = Entry(edit_window, width=20)
    edit_id.grid(column=0, row=2)
    edit_id.focus()
    btn = Button(edit_window, text="Edit", command=lambda:
    (edit_contact(edit_id)))
    btn.grid(column=1, row=2)


def edit_contact(edit_id: Entry):
    list_contact = load_database()
    edit_id_str = edit_id.get()
    for i in range(len(list_contact)):
        if edit_id_str == list_contact[i].id:
            new_edit_window, edit = \
                create_record_window(2, edit_id_str)
            edit.name.insert(END, list_contact[i].name)
            edit.address.insert(END, list_contact[i].address)
            edit.phone.insert(END, list_contact[i].phone)
            edit.id.insert(END, list_contact[i].id)


def confirm_edit_button(new_window: Tk, info: Person(Entry), i: int,
                        contact_id: str):
    btn = Button(new_window, text="Confirm", command=lambda:
    (show_message(), get_text(info, i, contact_id),
     new_window.destroy()))
    btn.grid(column=9, row=1)
