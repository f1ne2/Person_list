from app.view import *


class Flag:

    def __init__(self, flag):
        self.__flag = flag

    def define(self):
        if self.__flag == "1":
            return 1
        else:
            return 2


def main():
    flag = Flag(input(""))
    window = main_screen()
    button_add(window, flag.define())
    button_search(window, flag.define())
    button_view(window, flag.define())
    button_exit(window)
    window.mainloop()


print("Press 1 if you would like to work with file or press any another key, "
      "if you would you like work with database")
if __name__ == "__main__":
    main()
