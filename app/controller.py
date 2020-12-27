from view import *
from database import *
from Model import *
from Person import Person


def find_contact(self) -> Person:
    return find_database_contact(self.id_str)


def print_contacts(self) -> List[Person]:
    return get_all_contacts()


def del_contact(self):
    delete_contact(self.search_id_str)


def edt_contact(self):
    list_contacts = get_all_contacts()
    edit_contact(self.edit_id_str, self.info, list_contacts)


def load_for_add(self):
    add_contact(get_all_contacts(), self.new_contact_info)


def load_for_edit(self):
    write_ed_contact(get_all_contacts(), self.new_contact_info,
                     self.contact_id)


def load_for_add_db(self):
    insert_into_table(self.new_contact_info)


def load_for_edit_db(self):
    update_table(self.new_contact_info, self.contact_id)


def load_from_db_to_view(self) -> List[Person]:
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


def del_contact_sql_db(self):
    delete_from_table(self.search_id_str)


def edt_contact_sql_db(self):
    list_contacts = load_from_db_to_view(self)
    edit_contact(self.edit_id_str, self.info, list_contacts)


def find_contact_in_db(self) -> Person:
    tupl = select_from_db(self.search_id_str)
    find_info = Person()
    find_info.name = tupl[0][0]
    find_info.address = tupl[0][1]
    find_info.phone = tupl[0][2]
    find_info.id = tupl[0][3]
    return find_info


def init(self, id_str: str, info: Person):
    self.id_str = id_str
    self.info = info


class MetaFile(object):
    def __str__(self):
        return '<transfer_info-object/>'


attrs_file = {'find_contact': find_contact,'print_contacts': print_contacts,
              'del_contact': del_contact, 'edt_contact': edt_contact,
              'load_for_add': load_for_add, 'load_for_edit': load_for_edit,
              '__init__': init, 'load_for_add_db': load_for_add_db,
              'load_for_edit_db': load_for_edit_db,
              'load_from_db_to_view': load_from_db_to_view,
              'del_contact_sql_db': del_contact_sql_db,
              'edt_contact_sql_db': edt_contact_sql_db,
              'find_contact_in_db': find_contact_in_db}

bases = (MetaFile,)
TransferFile = type('transfer_info', bases, attrs_file)
transfer_info1 = TransferFile("1", info=None)
out = transfer_info1.find_contact()
print(out.name)