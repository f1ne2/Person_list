from app.view import *


def main():
    window = main_screen()
    button_add(window)
    button_search(window)
    button_view(window)
    button_exit(window)
    window.mainloop()


if __name__ == "__main__":
    main()
