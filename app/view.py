from controller import *
from database import *
from tkinter import *
from tkinter import messagebox


class ViewTkinter:
    def __init__(self, flag: int):
        if flag == 1:
            self.data1 = WorkWithFile()
        else:
            self.data1 = WorkWithDB()

    def create_record_window(self, i: int, contact_id: str) -> \
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
            self.confirm_add_button(new_window, info, 1)
        if i == 2:
            self.confirm_edit_button(new_window, info, 2, contact_id)
        return info

    def create_view_window(self):
        viewing_window = Tk()
        viewing_window.title("Contacts list review")
        viewing_window.geometry("750x250")
        lbl = Label(viewing_window, text="Contacts:",
                    font=("Times New Roman", 16))
        lbl.grid(column=0, row=0)
        self.del_butn(viewing_window)
        self.edit_butn(viewing_window)
        self.data_from_controller(viewing_window)

    def data_from_controller(self, viewing_window: Tk):
        self.output_contact(viewing_window,
                            Controller(self.data1).load_to_view())

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
        (self.output_find_contact(new_window,
                                  Controller(self.data1).
                                  find_contact(search_id.get()))))
        btn.grid(column=4, row=1)

    def create_delete_window(self):
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
        (Controller(self.data1).del_contact(search_id.get())))
        btn.grid(column=1, row=2)

    def create_edit_window(self):
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
        (Controller(self.data1).edt_contact(edit_id.get(),
                                            self.create_record_window
                                            (2, edit_id.get()))))
        btn.grid(column=1, row=2)

    def del_butn(self, view_contacts_window: Tk):
        btn = Button(view_contacts_window, text="Delete contact",
                     command=lambda: (self.create_delete_window()))
        btn.grid(column=3, row=0)

    def edit_butn(self, view_contacts_window: Tk):
        btn = Button(view_contacts_window, text="Edit contact",
                     command=self.create_edit_window)
        btn.grid(column=4, row=0)

    def confirm_add_button(self, new_window: Tk, info: Person(Entry), i: int):
        btn = Button(new_window, text="Confirm", command=lambda:
        (self.show_message(), self.get_text(info, i, ""), new_window.destroy()))
        btn.grid(column=9, row=1)

    def confirm_edit_button(self, new_window: Tk, info: Person(Entry), i: int,
                            contact_id: str):
        btn = Button(new_window, text="Confirm", command=lambda:
        (self.show_message(), self.get_text(info, i, contact_id),
         new_window.destroy()))
        btn.grid(column=9, row=1)

    def show_message(self):
        messagebox.showinfo(title="Information", message="Successful")

    def button_add(self, window: Tk):
        btn1 = Button(window, text="Add new contact",
                      command=lambda: (self.create_record_window(1, "")))
        btn1.grid(column=0, row=1)

    def button_search(self, window: Tk):
        btn4 = Button(window, text="Search contact",
                      command=lambda: (self.create_search_window()))
        btn4.grid(column=0, row=2)

    def button_view(self, window: Tk):
        btn5 = Button(window, text="View contact list",
                      command=lambda:
                      (self.create_view_window()))
        btn5.grid(column=0, row=3)

    def button_exit(self, window: Tk):
        btn6 = Button(window, text="Exit", command=window.quit)
        btn6.grid(column=0, row=4)

    def main_screen(self) -> Tk:
        window = Tk()
        window.title("Welcome to Contacts list")
        lbl = Label(window, text="Options:", font=("Times New Roman", 16))
        lbl.grid(column=0, row=0)
        window.geometry("500x250")
        return window

    def get_text(self, info: Person(Entry), i: int, contact_id: str):
        new_contact_info = Person()
        new_contact_info.name = info.name.get()
        new_contact_info.address = info.address.get()
        new_contact_info.phone = info.phone.get()
        new_contact_info.id = info.id.get()
        if i == 1:
            Controller(self.data1).load_for_add(new_contact_info)
        if i == 2:
            Controller(self.data1).load_for_edit(new_contact_info, contact_id)

    def output_find_contact(self, new_window: Tk, contact: Person):
        lbl = Label(new_window, text="Name: \t %s \t Address: \t %s \t "
                                     "Phone: \t %s \t ID:" "%s" % (contact.name,
                                                                   contact.address,
                                                                   contact.phone,
                                                                   contact.id),
                    font=("Times New Roman", 12))
        lbl.grid(column=0, row=4)

    def output_contact(self, view_contacts_window: Tk, contacts_list: list):
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

