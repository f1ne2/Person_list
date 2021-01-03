from Person import Person
from abstract import FormalParserInterface
import pickle
import os


class WorkWithFile(FormalParserInterface):
    def delete_from_table(self, delete_id_str: str) -> None:
        list_contact = self.get_all_contacts()
        if os.path.exists("database.dat"):
            for i in range(len(list_contact)):
                if delete_id_str == list_contact[i].id:
                    list_contact.pop(i)
                    break
            with open("database.dat", "wb") as file:
                pickle.dump(list_contact, file)

    def update_table(self, new_contact_info: Person, contact_id: str) -> None:
        list_contacts = self.get_all_contacts()
        for j in range(len(list_contacts)):
            if contact_id == list_contacts[j].id:
                list_contacts.remove(list_contacts[j])
                list_contacts.insert(j, new_contact_info)
                break
        self.write_all_contacts(list_contacts)

    def get_all_contacts(self) -> list:
        list_contacts = []
        if os.path.exists("database.dat"):
            with open("database.dat", "rb") as file:
                list_contacts = pickle.load(file)
            return list_contacts
        return list_contacts

    def write_all_contacts(self, database: list) -> None:
        with open("database.dat", "wb") as file:
            pickle.dump(database, file)

    def insert_into_table(self, new_contact_info: Person) -> None:
        list_contacts = self.get_all_contacts()
        list_contacts.append(new_contact_info)
        self.write_all_contacts(list_contacts)

    def select_from_db(self, search_id_str: str) -> Person:
        list_contacts = self.get_all_contacts()
        for i in range(len(list_contacts)):
            if search_id_str == list_contacts[i].id:
                return list_contacts[i]
