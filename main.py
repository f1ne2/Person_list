from app.view import *
from app.controller import *


class Flag:

    def __init__(self, flag):
        self.__flag = flag

    def define(self):
        if self.__flag == "1":
            return 1
        else:
            return 2


def main():
    flag = Flag(input())
    if flag.define() == 1:
        Controller(WorkWithFile().check_file_exist())
    else:
        Controller(WorkWithDB().check_file_exist())
    view2 = ViewTkinter(flag.define())
    window = view2.main_screen()
    view2.button_add(window)
    view2.button_search(window)
    view2.button_view(window)
    view2.button_exit(window)
    Controller(WorkWithDB()).create_table()
    window.mainloop()


print("Press 1 if you would like to work with file or press any another key, "
      "if you would you like work with database")

if __name__ == "__main__":
    main()
