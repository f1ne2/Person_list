from controller import *
from database import *
from tkinter import *
from tkinter import messagebox


def create_record_window(i: int, contact_id: str, flag: int) -> Person(Entry):
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
        confirm_add_button(new_window, info, 1, flag)
    if i == 2:
        confirm_edit_button(new_window, info, 2, contact_id, flag)
    return info


def create_view_window(flag: int):
    viewing_window = Tk()
    viewing_window.title("Contacts list review")
    viewing_window.geometry("750x250")
    lbl = Label(viewing_window, text="Contacts:",
                font=("Times New Roman", 16))
    lbl.grid(column=0, row=0)
    del_butn(viewing_window, flag)
    edit_butn(viewing_window, flag)
    data_from_controller(viewing_window, flag)


def data_from_controller(viewing_window: Tk, flag: int):
    if flag == 1:
        output_contact(viewing_window, print_contacts())
    else:
        output_contact(viewing_window, load_from_db_to_view())


def create_search_window(flag: int):
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
    if flag == 1:
        btn = Button(new_window, text="Search ID", command=lambda:
        (output_find_contact(new_window, find_contact(search_id.get()))))
        btn.grid(column=4, row=1)
    else:
        btn = Button(new_window, text="Search ID", command=lambda:
        (output_find_contact(new_window, find_contact_in_db(search_id.get()))))
        btn.grid(column=4, row=1)


def create_delete_window(flag: int):
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
    if flag == 1:
        btn = Button(new_window, text="Delete", command=lambda:
        (del_contact(search_id.get())))
        btn.grid(column=1, row=2)
    else:
        btn = Button(new_window, text="Delete", command=lambda:
        (del_contact_sql_db(search_id.get())))
        btn.grid(column=1, row=2)


def create_edit_window(flag: int):
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
    if flag == 1:
        btn = Button(edit_window, text="Edit", command=lambda:
        (edt_contact(edit_id.get(), create_record_window(2, edit_id.get(),
                                                         flag))))
        btn.grid(column=1, row=2)
    else:
        btn = Button(edit_window, text="Edit", command=lambda:
        (edt_contact_sql_db(edit_id.get(),
                            create_record_window(2, edit_id.get(), flag))))
        btn.grid(column=1, row=2)


def del_butn(view_contacts_window: Tk, flag: int):
    btn = Button(view_contacts_window, text="Delete contact",
                 command=lambda: (create_delete_window(flag)))
    btn.grid(column=3, row=0)


def edit_butn(view_contacts_window: Tk, flag: int):
    btn = Button(view_contacts_window, text="Edit contact",
                 command=lambda: (create_edit_window(flag)))
    btn.grid(column=4, row=0)


def confirm_add_button(new_window: Tk, info: Person(Entry), i: int, flag: int):
    btn = Button(new_window, text="Confirm", command=lambda:
    (show_message(), get_text(info, i, "", flag), new_window.destroy()))
    btn.grid(column=9, row=1)


def confirm_edit_button(new_window: Tk, info: Person(Entry), i: int,
                        contact_id: str, flag: int):
    btn = Button(new_window, text="Confirm", command=lambda:
    (show_message(), get_text(info, i, contact_id, flag),
     new_window.destroy()))
    btn.grid(column=9, row=1)


def show_message():
    messagebox.showinfo(title="Information", message="Successful")


def button_add(window: Tk, flag: int):
    btn1 = Button(window, text="Add new contact",
                  command=lambda: (create_record_window(1, "", flag)))
    btn1.grid(column=0, row=1)


def button_search(window: Tk, flag: int):
    btn4 = Button(window, text="Search contact",
                  command=lambda: (create_search_window(flag)))
    btn4.grid(column=0, row=2)


def button_view(window: Tk, flag: int):
    btn5 = Button(window, text="View contact list",
                  command=lambda:
                  (create_view_window(flag)))
    btn5.grid(column=0, row=3)


def button_exit(window: Tk):
    btn6 = Button(window, text="Exit", command=window.quit)
    btn6.grid(column=0, row=4)


def main_screen() -> Tk:
    window = Tk()
    window.title("Welcome to Contacts list")
    lbl = Label(window, text="Options:", font=("Times New Roman", 16))
    lbl.grid(column=0, row=0)
    window.geometry("500x250")
    return window


def get_text(info: Person(Entry), i: int, contact_id: str, flag: int):
    new_contact_info = Person()
    new_contact_info.name = info.name.get()
    new_contact_info.address = info.address.get()
    new_contact_info.phone = info.phone.get()
    new_contact_info.id = info.id.get()
    if flag == 1 and i == 1:
        load_for_add(new_contact_info)
    if flag == 1 and i == 2:
        load_for_edit(new_contact_info, contact_id)
    if flag == 2 and i == 1:
        load_for_add_db(new_contact_info)
    if flag == 2 and i == 2:
        load_for_edit_db(new_contact_info, contact_id)


def output_find_contact(new_window: Tk, contact: Person):
    lbl = Label(new_window, text="Name: \t %s \t Address: \t %s \t Phone: \t"
                                 " %s \t ID:" "%s" % (contact.name,
                                                      contact.address,
                                                      contact.phone,
                                                      contact.id),
                font=("Times New Roman", 12))
    lbl.grid(column=0, row=4)


def output_contact(view_contacts_window: Tk, contacts_list: list):
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


def edit_contact(edit_id_str: str, edit: Person, list_contacts: list):
    for i in range(len(list_contacts)):
        if edit_id_str == list_contacts[i].id:
            edit.name.insert(END, list_contacts[i].name)
            edit.address.insert(END, list_contacts[i].address)
            edit.phone.insert(END, list_contacts[i].phone)
            edit.id.insert(END, list_contacts[i].id)