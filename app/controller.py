from view import *
from database import *
from Model import *
from Person import Person


def find_contact(search_id_str: str) -> Person:
    return find_database_contact(search_id_str)


def print_contacts() -> List[Person]:
    return get_all_contacts()


def del_contact(search_id_str: str):
    delete_contact(search_id_str)


def edt_contact(edit_id_str: str, info: Person):
    list_contacts = get_all_contacts()
    edit_contact(edit_id_str, info, list_contacts)


def load_for_add(new_contact_info: Person):
    add_contact(get_all_contacts(), new_contact_info)


def load_for_edit(new_contact_info: Person, contact_id: str):
    write_ed_contact(get_all_contacts(), new_contact_info, contact_id)


def load_for_add_db(new_contact_info: Person):
    insert_into_table(new_contact_info)


def load_for_edit_db(new_contact_info: Person, contact_id: str):
    update_table(new_contact_info, contact_id)


def load_from_db_to_view() -> List[Person]:
    out_info = Person()
    out_list = []
    tupl = load_sql_database()
    for i in range(len(tupl)):
        out_info.name = tupl[i][0]
        out_info.address = tupl[i][1]
        out_info.phone = tupl[i][2]
        out_info.id = tupl[i][3]
        out_list.append(out_info)
        out_info = Person()
    return out_list


def del_contact_sql_db(search_id_str: str):
    delete_from_table(search_id_str)


def edt_contact_sql_db(edit_id_str: str, info: Person):
    list_contacts = load_from_db_to_view()
    edit_contact(edit_id_str, info, list_contacts)


def find_contact_in_db(search_id_str: str) -> Person:
    tupl = select_from_db(search_id_str)
    find_info = Person()
    find_info.name = tupl[0][0]
    find_info.address = tupl[0][1]
    find_info.phone = tupl[0][2]
    find_info.id = tupl[0][3]
    return find_info









