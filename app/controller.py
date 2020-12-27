from view import *
from database import *
from Model import *
from Person import Person


def find_contact(search_id_str: str) -> Person:
    find = WorkWithFile()
    return find.select_from_db(search_id_str)


def print_contacts() -> List[Person]:
    prnt = WorkWithFile()
    return prnt.get_all_contacts()


def del_contact_sql_db(search_id_str: str):
    delete = WorkWithDB()
    delete.delete_from_table(search_id_str)


def del_contact(search_id_str: str):
    delete = WorkWithFile()
    delete.delete_from_table(search_id_str)


def edt_contact(edit_id_str: str, info: Person):
    edt = WorkWithFile()
    list_contacts = edt.get_all_contacts()
    edit_contact(edit_id_str, info, list_contacts)


def load_for_add(new_contact_info: Person):
    load_add = WorkWithFile()
    load_add.insert_into_table(new_contact_info)


def load_for_edit(new_contact_info: Person, contact_id: str):
    load_edit = WorkWithFile()
    load_edit.update_table(new_contact_info, contact_id)


def load_for_add_db(new_contact_info: Person):
    load_add_db = WorkWithDB()
    load_add_db.insert_into_table(new_contact_info)


def load_for_edit_db(new_contact_info: Person, contact_id: str):
    load_edit_db = WorkWithDB()
    load_edit_db.update_table(new_contact_info, contact_id)


def load_from_db_to_view() -> List[Person]:
    load_from_db = WorkWithDB()
    return load_from_db.get_all_contacts()


def edt_contact_sql_db(edit_id_str: str, info: Person):
    list_contacts = load_from_db_to_view()
    edit_contact(edit_id_str, info, list_contacts)


def find_contact_in_db(search_id_str: str) -> Person:
    select_db = WorkWithDB()
    return select_db.select_from_db(search_id_str)
