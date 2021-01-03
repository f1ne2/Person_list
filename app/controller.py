from Model import *
from Person import Person
from typing import List


class Controller:
    def __init__(self, storage: FormalParserInterface):
        self.storage = storage

    def find_contact(self, search_id_str: str) -> Person:
        return self.storage.select_from_db(search_id_str)

    def del_contact(self, search_id_str: str) -> None:
        self.storage.delete_from_table(search_id_str)

    def load_for_add(self, new_contact_info: Person) -> None:
        self.storage.insert_into_table(new_contact_info)

    def load_for_edit(self, new_contact_info: Person, contact_id: str) -> None:
        self.storage.update_table(new_contact_info, contact_id)

    def load_to_view(self) -> List[Person]:
        return self.storage.get_all_contacts()

    def edt_contact(self, edit_id_str: str, info: Person) -> None:
        list_contacts = self.storage.get_all_contacts()
        self.edit_contact(edit_id_str, info, list_contacts)

    def edit_contact(self, edit_id_str: str, edit: Person,
                     list_contacts: list) -> None:
        for i in range(len(list_contacts)):
            if edit_id_str == list_contacts[i].id:
                edit.name.insert("end", list_contacts[i].name)
                edit.address.insert("end", list_contacts[i].address)
                edit.phone.insert("end", list_contacts[i].phone)
                edit.id.insert("end", list_contacts[i].id)

    def create_table(self) -> None:
        self.storage.create_table()
