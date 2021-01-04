from abstract import *
import pickle
import os


class WorkWithFile(FormalParserInterface):

    def delete_from_table(self, delete_id_str: str) -> int:
        j = 0
        list_contact = self.get_all_contacts()
        if os.path.exists(file_2):
            for i in range(len(list_contact)):
                if delete_id_str == list_contact[i].id:
                    list_contact.pop(i)
                    j = 1
                    break
            if j == 0:
                return 2
            with open(file_2, "wb") as file:
                pickle.dump(list_contact, file)
            return 1

    def update_table(self, new_contact_info: Person, contact_id: str) -> int:
        list_contacts = self.get_all_contacts()
        i = 0
        for j in range(len(list_contacts)):
            if contact_id == list_contacts[j].id and new_contact_info.id == \
                    list_contacts[j].id:
                list_contacts.remove(list_contacts[j])
                list_contacts.insert(j, new_contact_info)
                i = 1
                break
        if i == 0:
            return 2
        self.write_all_contacts(list_contacts)
        return 1

    def get_all_contacts(self) -> List[Person]:
        list_contacts = []
        if os.path.exists(file_2):
            with open(file_2, "rb") as file:
                list_contacts = pickle.load(file)
            return list_contacts
        return list_contacts

    def write_all_contacts(self, database: List[Person]) -> None:
        with open(file_2, "wb") as file:
            pickle.dump(database, file)

    def insert_into_table(self, new_contact_info: Person) -> int:
        list_contacts = self.get_all_contacts()
        for i in range(len(list_contacts)):
            if new_contact_info.id == list_contacts[i].id:
                return 2
        list_contacts.append(new_contact_info)
        self.write_all_contacts(list_contacts)
        return 1

    def select_from_db(self, search_id_str: str) -> Person:

        list_contacts = self.get_all_contacts()
        for i in range(len(list_contacts)):
            if search_id_str == list_contacts[i].id:
                return list_contacts[i]
        return Person("", "", "", "")

    def create_table(self) -> None:
        pass


file_2 = "database.dat"