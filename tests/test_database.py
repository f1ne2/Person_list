import unittest
from app.database import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.person_info = Person()
        self.person_info.name = "Alex"
        self.person_info.address = "T"
        self.person_info.phone = "+375"
        self.person_info.id = "22"

    def test_insert_into_table(self):
        self.sql = WorkWithDB()
        self.sql.insert_into_table(self.person_info)
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id=22")
        cursor_out = cursor.fetchall()
        self.assertEqual(cursor_out, [('Alex', 'T', '+375',
                                       '22')])

    def test_update_table(self):
        self.sql = WorkWithDB()
        self.sql.insert_into_table(self.person_info)
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()
        self.new_person_info = Person('Olga', 'Minsk', '+375', '33')
        self.sql.update_table(self.new_person_info, '22')
        cursor.execute("SELECT * FROM contacts WHERE id=33")
        cursor_out = cursor.fetchone()
        self.assertEqual(cursor_out, ('Olga', 'Minsk', '+375', '33'))
        self.sql.delete_from_table('33')

    def test_delete_from_table(self):
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()
        self.sql = WorkWithDB()
        self.sql.delete_from_table('33')
        self.res = cursor.execute("SELECT * FROM contacts WHERE id=33")
        conn.commit()
        cursor_out = cursor.fetchall()
        self.assertEqual(cursor_out, [])

    def test_select_from_db(self):
        self.sql = WorkWithDB()
        self.sql.insert_into_table(self.person_info)
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()
        info = self.sql.select_from_db('22')
        self.assertEqual(info.name, self.person_info.name)
        self.assertEqual(info.address, self.person_info.address)
        self.assertEqual(info.phone, self.person_info.phone)
        self.assertEqual(info.id, self.person_info.id)
        self.sql.delete_from_table('22')

    def test_get_all_contact(self):
        self.sql = WorkWithDB()
        self.sql.insert_into_table(self.person_info)
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()
        list_contacts = self.sql.get_all_contacts()
        self.assertEqual(list_contacts[0].name, self.person_info.name)
        self.assertEqual(list_contacts[0].address, self.person_info.address)
        self.assertEqual(list_contacts[0].phone, self.person_info.phone)
        self.assertEqual(list_contacts[0].id, self.person_info.id)
        self.sql.delete_from_table('22')




if __name__ == "__main__":
    unittest.main()






