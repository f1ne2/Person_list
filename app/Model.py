from Person import Person
import pickle
import os


def delete_contact(delete_id_str: str):
    list_contact = get_all_contacts()
    if os.path.exists("database.dat"):
        for i in range(len(list_contact)):
            if delete_id_str == list_contact[i].id:
                list_contact.pop(i)
                break
        with open("database.dat", "wb") as file:
            pickle.dump(list_contact, file)
    else:
        pass


def get_all_contacts() -> list:
    list_contacts = []
    if os.path.exists("database.dat"):
        file = open("database.dat", "rb")
        while 1:
            try:
                list_contacts = pickle.load(file)
            except EOFError:
                break
        file.close()
        return list_contacts
    return list_contacts


def write_all_contacts(database: list):
    with open("database.dat", "wb") as file:
        pickle.dump(database, file)


def add_contact(list_contacts, new_contact_info):
    list_contacts.append(new_contact_info)
    write_all_contacts(list_contacts)


def write_ed_contact(list_contacts: list, new_contact_info: Person,
                     contact_id: str):
    for j in range(len(list_contacts)):
        if contact_id == list_contacts[j].id:
            list_contacts.remove(list_contacts[j])
            list_contacts.insert(j, new_contact_info)
            break
    write_all_contacts(list_contacts)


def find_database_contact(search_id_str: str) -> Person:
    list_contacts = get_all_contacts()
    for i in range(len(list_contacts)):
        if search_id_str == list_contacts[i].id:
            return list_contacts[i]

