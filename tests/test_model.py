import unittest
from app.Model import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.person_info = Person("Alex", "T", "+37529", "22")
        self.file = WorkWithFile()

    def test_insert_into_table(self):
        self.file.insert_into_table(self.person_info)
        info = self.file.get_all_contacts()
        self.assertEqual(info[0], self.person_info)

    def test_delete_from_table(self):
        self.file.delete_from_table("22")
        self.assertEqual(self.file.get_all_contacts(), [])

    def test_get_all_contact(self):
        self.assertEqual(self.file.get_all_contacts(), [])

    def test_update_table(self):
        self.file.insert_into_table(self.person_info)
        new_contact_info = Person("Olga", "A", "+37529", "22")
        self.file.update_table(new_contact_info, "22")
        list_contact = self.file.get_all_contacts()
        self.assertEqual(list_contact[0], new_contact_info)

    def test_select_from_db(self):
        new_contact_info = Person("Olga", "A", "+37529", "23")
        self.file.insert_into_table(new_contact_info)
        info = self.file.select_from_db("23")
        self.assertEqual(info, new_contact_info)
        self.file.delete_from_table("23")
