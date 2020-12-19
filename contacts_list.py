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
    def create_window(self):
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

    def get_text(self, info):
        res_info = Person()
        res_info.name = info.name.get()
        res_info.address = info.address.get()
        res_info.phone = info.phone.get()
        res_info.id = info.id.get()
        self.save(res_info)

    def confirm_button(self, new_window, info):
        btn = Button(new_window, text="Confirm", command=lambda:
        [self.show_message(), self.get_text(info), new_window.destroy()])
        btn.grid(column=9, row=1)

    def del_contact(self):
        a =0
    def edit_contact(self):
        a = 0

    def search_contact(self):
        a = 0

    def view_contacts(self):
        info = Person()
        with open("database.dat", "rb") as file:
            person_info = pickle.load(file)
            for item in person_info:
                print(item)
        
    def scroled_text(self, window):
        txt = scrolledtext.ScrolledText(window, width=40, height=10)

    def show_message(self):
        messagebox.showinfo(title="Information", message="Successful")

    def save(self, res_info):
        with open("database.dat", "ab") as file:
            pickle.dump(res_info.name, file)
            pickle.dump(res_info.address, file)
            pickle.dump(res_info.phone, file)
            pickle.dump(res_info.id, file)

    def button_add(self, window):
        btn1 = Button(window, text="Add new contact",
                      command=self.create_window)
        btn1.grid(column=0, row=1)

    def button_2(self, window):
        btn2 = Button(window, text="Edit contact")
        btn2.grid(column=0, row=2)

    def button_3(self, window):
        btn3 = Button(window, text="Delete contact")
        btn3.grid(column=0, row=3)

    def button_4(self, window):
        btn4 = Button(window, text="Search contact")
        btn4.grid(column=0, row=4)

    def button_view(self, window):
        btn5 = Button(window, text="View contact list",
                      command=self.view_contacts)
        btn5.grid(column=0, row=5)

    def button_6(self, window):
        btn6 = Button(window, text="Exit", command=window.quit)
        btn6.grid(column=0, row=6)

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
    app.button_2(window)
    app.button_3(window)
    app.button_4(window)
    app.button_view(window)
    app.button_6(window)
    window.mainloop()


if __name__ == "__main__":
    main()
