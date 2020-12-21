from app.contact_review import *
from tkinter import *
import pickle


def create_delete_window():
    new_window = Tk()
    new_window.title("Welcome to Contacts list")
    new_window.geometry("500x250")
    lbl = Label(new_window, text="If you want to delete contact,"
                                 "enter contact's ID and press Delete",
                font=("Times New Roman", 12))
    lbl.grid(column=0, row=0)
    search_id = Entry(new_window, width=20)
    search_id.grid(column=0, row=2)
    search_id.focus()
    btn = Button(new_window, text="Delete",
                 command=lambda: (delete_contact(search_id)))
    btn.grid(column=1, row=2)


def delete_contact(delete_id: Entry):
    list_contact = load_database()
    delete_id_str = delete_id.get()
    for i in range(len(list_contact)):
        if delete_id_str == list_contact[i].id:
            list_contact.pop(i)
            break
    with open("database.dat", "wb") as file:
        pickle.dump(list_contact, file)

