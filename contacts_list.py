import pickle
import os
from tkinter import *
from tkinter import messagebox
from typing import List


class Person:

    def __init__(self, name=None, address=None, phone=None,
                 identification=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.id = identification


class Application:
    def create_record_window(self) -> Tk and Person(Entry):
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

        self.confirm_button(new_window, info)

        return new_window, info

    def create_view_window(self):
        viewing_window = Tk()
        viewing_window.title("Contacts list review")
        viewing_window.geometry("750x250")
        lbl = Label(viewing_window, text="Contacts:",
                    font=("Times New Roman", 16))
        lbl.grid(column=0, row=0)
        list_contacts = self.load_database()
        self.print_contacts(viewing_window, list_contacts)

    def create_search_window(self):
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
        [self.get_id(search_id, new_window)])
        btn.grid(column=4, row=1)

    def get_id(self, search_id: Entry, new_window: Tk):
        search_id_str = search_id.get()
        self.print_find_contact(search_id_str, new_window)

    def print_find_contact(self, search_id_str: str, new_window: Tk):
        database = self.load_database()
        for i in range(len(database[0])):
            if search_id_str == database[0][i].id:
                lbl = Label(new_window,
                            text="Name: \t %s \t Address: "
                                 "\t %s \t" "Phone: \t %s "
                                 "\t ID:" "%s" %
                                 (database[0][i].name,
                                  database[0][i].address,
                                  database[0][i].phone,
                                  database[0][i].id),
                            font=("Times New Roman", 12))
                lbl.grid(column=0, row=i+4)

    def print_contacts(self, view_contacts_window: Tk,
                       contacts_list: List[list]):
        for i in range(len(contacts_list[0])):
            lbl = Label(view_contacts_window, text="Name: \t %s \t Address: "
                                                   "\t %s \t" "Phone: \t %s "
                                                   "\t ID:" "%s" %
                                                  (contacts_list[0][i].name,
                                                   contacts_list[0][i].address,
                                                   contacts_list[0][i].phone,
                                                   contacts_list[0][i].id),
                        font=("Times New Roman", 12))
            lbl.grid(column=0, row=i+2)
            self.del_butn(view_contacts_window, i)
            self.edit_butn(view_contacts_window, i)

    def del_butn(self, view_contacts_window: Tk, i: int):
        btn = Button(view_contacts_window, text="Delete contact",
                     command=self.create_delete_window)
        btn.grid(column=4, row=i+2)

    def create_delete_window(self):
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
        btn = Button(new_window, text="Delete")
        btn.grid(column=1, row=2)

    # def delete_contact(self, new_window, search_id):
    #     list_contact = self.load_database()
    #     search_id_str = search_id.get()
    #     for i in range(len(list_contact[0])):
    #         if search_id_str == list_contact[0][i].id:
    #             list_contact.remove(list_contact[0][i])
    #     with open("database.dat", "wb") as file:
    #         pickle.dump(list_contact, file)

    def edit_butn(self, view_contacts_window: Tk, i: int):
        btn = Button(view_contacts_window, text="Edit contact")
        btn.grid(column=8, row=i+2)

    def get_text(self, info: Person(Entry)):
        new_contact_info = Person()
        new_contact_info.name = info.name.get()
        new_contact_info.address = info.address.get()
        new_contact_info.phone = info.phone.get()
        new_contact_info.id = info.id.get()
        self.save(new_contact_info)

    def confirm_button(self, new_window: Tk, info: Person(Entry)):
        btn = Button(new_window, text="Confirm", command=lambda:
        (self.show_message(), self.get_text(info), new_window.destroy()))
        btn.grid(column=9, row=1)

    def load_database(self):
        list_contacts = []
        file = open("database.dat", "rb")
        while 1:
            try:
                list_contacts.append(pickle.load(file))
            except EOFError:
                break
        file.close()
        return list_contacts

    def show_message(self):
        messagebox.showinfo(title="Information", message="Successful")

    def save(self, new_contact_info: Person(Entry)):
        if os.path.exists("database.dat"):
            with open("database.dat", "rb") as file:
                load_database = pickle.load(file)
                load_database.append(new_contact_info)
        else:
            load_database = []
            load_database.append(new_contact_info)
        with open("database.dat", "wb") as file:
            pickle.dump(load_database, file)

    def button_add(self, window: Tk):
        btn1 = Button(window, text="Add new contact",
                      command=self.create_record_window)
        btn1.grid(column=0, row=1)

    def button_search(self, window: Tk):
        btn4 = Button(window, text="Search contact",
                      command=self.create_search_window)
        btn4.grid(column=0, row=2)

    def button_view(self, window: Tk):
        btn5 = Button(window, text="View contact list",
                      command=self.create_view_window)
        btn5.grid(column=0, row=3)

    def button_exit(self, window: Tk):
        btn6 = Button(window, text="Exit", command=window.quit)
        btn6.grid(column=0, row=4)

    def main_screen(self):
        window = Tk()
        window.title("Welcome to Contacts list")
        lbl = Label(window, text="Options:", font=("Times New Roman", 16))
        lbl.grid(column=0, row=0)
        window.geometry("500x250")
        return window


def main():
    app = Application()
    window = app.main_screen()
    app.button_add(window)
    app.button_search(window)
    app.button_view(window)
    app.button_exit(window)
    window.mainloop()


if __name__ == "__main__":
    main()
