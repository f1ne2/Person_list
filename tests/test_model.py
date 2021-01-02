import unittest
from app.Model import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.person_info = Person("Alex", "T", "+37529", "22")

    def test_insert_into_table(self):
        self.file = WorkWithFile()
        self.file.insert_into_table(self.person_info)
        info = self.file.get_all_contacts()
        self.assertEqual(info[0].name, self.person_info.name)
        self.assertEqual(info[0].address, self.person_info.address)
        self.assertEqual(info[0].phone, self.person_info.phone)
        self.assertEqual(info[0].id, self.person_info.id)

    def test_delete_from_table(self):
        self.file = WorkWithFile()
        self.file.delete_from_table("22")
        self.assertEqual(self.file.get_all_contacts(), [])

    def test_get_all_contact(self):
        self.file = WorkWithFile()
        self.assertEqual(self.file.get_all_contacts(), [])

    def test_update_table(self):
        self.file = WorkWithFile()
        self.file.insert_into_table(self.person_info)
        self.new_contact_info = Person("Olga", "A", "+37529", "23")
        self.file.update_table(self.new_contact_info, "22")
        list_contact = self.file.get_all_contacts()
        self.assertEqual(list_contact[0].name, self.new_contact_info.name)
        self.assertEqual(list_contact[0].address, self.new_contact_info.address)
        self.assertEqual(list_contact[0].phone,
                         self.new_contact_info.phone)
        self.assertEqual(list_contact[0].id, self.new_contact_info.id)

    def test_select_from_db(self):
        self.file = WorkWithFile()
        self.new_contact_info = Person("Olga", "A", "+37529", "23")
        self.file.insert_into_table(self.new_contact_info)
        info = self.file.select_from_db("23")
        self.assertEqual(info.name, self.new_contact_info.name)
        self.assertEqual(info.address, self.new_contact_info.address)
        self.assertEqual(info.phone, self.new_contact_info.phone)
        self.assertEqual(info.id, self.new_contact_info.id)
        self.file.delete_from_table("23")















