from Person import Person
from typing import List
from abc import ABCMeta, abstractmethod


class FormalParserInterface(metaclass=ABCMeta):
    @abstractmethod
    def delete_from_table(self, delete_id_str: str) -> Person:
        pass

    @abstractmethod
    def update_table(self, new_contact_info: Person, contact_id: str):
        pass

    @abstractmethod
    def get_all_contacts(self) -> List[Person]:
        pass

    @abstractmethod
    def insert_into_table(self, new_contact_info: Person):
        pass

    @abstractmethod
    def select_from_db(self, search_id_str: str) -> Person:
        pass
