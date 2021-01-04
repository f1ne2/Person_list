from Model import *
from database import *
from typing import List


class Controller:
    def __init__(self, storage: FormalParserInterface):
        self.storage = storage

    def find_contact(self, search_id_str: str) -> Person:
        return self.storage.select_from_db(search_id_str)

    def del_contact(self, search_id_str: str) -> int:
        return self.storage.delete_from_table(search_id_str)

    def load_for_add(self, new_contact_info: Person) -> int:
        return self.storage.insert_into_table(new_contact_info)

    def load_for_edit(self, new_contact_info: Person, contact_id: str) -> int:
        return self.storage.update_table(new_contact_info, contact_id)

    def load_to_view(self) -> List[Person]:
        return self.storage.get_all_contacts()

    def edt_contact(self, edit_id_str: str) -> Person:
        return self.storage.select_from_db(edit_id_str)

    def create_table(self) -> None:
        self.storage.create_table()

    def fill_edit_contact(self, edit_id_str: str) -> Person:
        return self.storage.select_from_db(edit_id_str)