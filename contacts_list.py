import pickle
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox


class Person:

    def __init__(self, name=None, address=None, phone=None,
                 identification=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.id = identification


class Application:
    def add_contact(self):
        window_add = Tk()
        window_add.title("Welcome to Contacts list")

        lbl = Label(window_add, text="Options:", font=("Times New Roman", 16))
        lbl.grid(column=0, row=0)
        window_add.geometry("1000x250")

        lbl = Label(window_add, text="Name:", font=("Times New Roman", 16))
        lbl.grid(column=1, row=1)

        txt1 = Entry(window_add, width=20)
        txt1.grid(column=2, row=1)
        txt1.focus()

        lbl = Label(window_add, text="Address:", font=("Times New Roman", 16))
        lbl.grid(column=3, row=1)

        txt2 = Entry(window_add, width=20)
        txt2.grid(column=4, row=1)

        lbl = Label(window_add, text="Phone:", font=("Times New Roman", 16))
        lbl.grid(column=5, row=1)

        txt3 = Entry(window_add, width=20)
        txt3.grid(column=6, row=1)

        lbl = Label(window_add, text="ID:", font=("Times New Roman", 16))
        lbl.grid(column=7, row=1)

        txt4 = Entry(window_add, width=20)
        txt4.grid(column=8, row=1)

        btn = Button(window_add, text="Confirm",
                     command=lambda: [self.show_message(),
                                      self.save(txt1, txt2, txt3, txt4),
                                      window_add.destroy()])
        btn.grid(column=9, row=1)

    def del_contact(self):
        a =0
    def edit_contact(self):
        a = 0

    def search_contact(self):
        a = 0

    def view_contacts(self):
        with open("database.dat", "rb") as file:
            person_info = pickle.load(file)
            information = "Name: %s \t Address: %s \t Phone: %s \t " \
                          "ID: %s" % (person_info.name, person_info.address,
                                      person_info.phone, person_info.id)
            print(information)

    def scroled_text(self):
        txt = scrolledtext.ScrolledText(window, width=40, height=10)

    def show_message(self):
        messagebox.showinfo("Information", "Successful")

    def save(self, name, address, phone, id):
        info = Person()
        info.name = name.get()
        info.address = address.get()
        info.phone = phone.get()
        info.id = id.get()
        with open("database.dat", "ab") as file:
            pickle.dump(info, file)

    def button_1(self):
        btn1 = Button(window, text="Add new contact", command=self.add_contact)
        btn1.grid(column=0, row=1)

    def button_2(self):
        btn2 = Button(window, text="Edit contact", command=self.edit_contact)
        btn2.grid(column=0, row=2)

    def button_3(self):
        btn3 = Button(window, text="Delete contact", command=self.del_contact)
        btn3.grid(column=0, row=3)

    def button_4(self):
        btn4 = Button(window, text="Search contact",
                      command=self.search_contact)
        btn4.grid(column=0, row=4)

    def button_5(self):
        btn5 = Button(window, text="View contact list",
                      command=self.view_contacts)
        btn5.grid(column=0, row=5)

    def button_6(self):
        btn6 = Button(window, text="Exit", command=window.quit)
        btn6.grid(column=0, row=6)


def main():
    app = Application()
    app.button_1()
    app.button_2()
    app.button_3()
    app.button_4()
    app.button_5()
    app.button_6()
    window.mainloop()


window = Tk()
window.title("Welcome to Contacts list")
lbl = Label(window, text="Options:", font=("Times New Roman", 16))
lbl.grid(column=0, row=0)
window.geometry("500x250")

if __name__ == "__main__":
    main()
