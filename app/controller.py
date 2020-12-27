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





    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     return (hasattr(subclass, 'find_contact') and
    #             callable(subclass.find_contact) and
    #             hasattr(subclass, 'extract_text') and
    #             callable(subclass.extract_text) or
    #             NotImplemented)


# def init(self, id_str: str, info: Person):
#     self.id_str = id_str
#     self.info = info
#
#
# class MetaFile(object):
#     def __str__(self):
#         return '<transfer_info-object/>'
#
#
# attrs_file = {'find_contact': find_contact,'print_contacts': print_contacts,
#               'del_contact': del_contact, 'edt_contact': edt_contact,
#               'load_for_add': load_for_add, 'load_for_edit': load_for_edit,
#               '__init__': init, 'load_for_add_db': load_for_add_db,
#               'load_for_edit_db': load_for_edit_db,
#               'load_from_db_to_view': load_from_db_to_view,
#               'del_contact_sql_db': del_contact_sql_db,
#               'edt_contact_sql_db': edt_contact_sql_db,
#               'find_contact_in_db': find_contact_in_db}
#
# bases = (MetaFile,)
# TransferFile = type('transfer_info', bases, attrs_file)
# transfer_info1 = TransferFile("1", info=None)
# out = transfer_info1.find_contact()
# print(out.name)