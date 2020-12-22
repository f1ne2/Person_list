from app.controller import *
from tkinter import *
from tkinter import messagebox


def create_record_window(i: int, contact_id: str) -> Tk and Person(Entry):
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
    (get_id(search_id, new_window)))
    btn.grid(column=4, row=1)


def create_delete_window():
    new_window = Tk()
    new_window.title("Welcome to Contacts list")
    new_window.geometry("500x250")
    lbl = Label(new_window, text="If you want to delete contact,enter "
                                 "contact's ID and press Delete",
                font=("Times New Roman", 12))
    lbl.grid(column=0, row=0)
    search_id = Entry(new_window, width=20)
    search_id.grid(column=0, row=2)
    search_id.focus()
    btn = Button(new_window, text="Delete", command=lambda:
    (delete_contact(search_id)))
    btn.grid(column=1, row=2)


def create_edit_window():
    edit_window = Tk()
    edit_window.title("Welcome to Contacts list")
    edit_window.geometry("500x250")
    lbl = Label(edit_window, text="If you want to edit contact, enter "
                                  "contact's ID and press Edit",
                font=("Times New Roman", 12))
    lbl.grid(column=0, row=0)
    edit_id = Entry(edit_window, width=20)
    edit_id.grid(column=0, row=2)
    edit_id.focus()
    btn = Button(edit_window, text="Edit", command=lambda:
    (edit_contact(edit_id)))
    btn.grid(column=1, row=2)


def del_butn(view_contacts_window: Tk):
    btn = Button(view_contacts_window, text="Delete contact",
                 command=create_delete_window)
    btn.grid(column=3, row=0)


def edit_butn(view_contacts_window: Tk):
    btn = Button(view_contacts_window, text="Edit contact",
                 command=create_edit_window)
    btn.grid(column=4, row=0)


def confirm_add_button(new_window: Tk, info: Person(Entry), i: int):
    btn = Button(new_window, text="Confirm", command=lambda:
    (show_message(), get_text(info, i, "0"), new_window.destroy()))
    btn.grid(column=9, row=1)


def confirm_edit_button(new_window: Tk, info: Person(Entry), i: int,
                        contact_id: str):
    btn = Button(new_window, text="Confirm", command=lambda:
    (show_message(), get_text(info, i, contact_id),
     new_window.destroy()))
    btn.grid(column=9, row=1)


def show_message():
    messagebox.showinfo(title="Information", message="Successful")


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


def get_id(search_id: Entry, new_window: Tk):
    search_id_str = search_id.get()
    print_find_contact(search_id_str, new_window)


def get_text(info: Person(Entry), i: int, contact_id: str):
    new_contact_info = Person()
    new_contact_info.name = info.name.get()
    new_contact_info.address = info.address.get()
    new_contact_info.phone = info.phone.get()
    new_contact_info.id = info.id.get()
    save(new_contact_info, i, contact_id)
