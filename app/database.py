import sqlite3
from typing import List
from Person import Person
from abstract import FormalParserInterface


class WorkWithDB(FormalParserInterface):
    def insert_into_table(self, new_contact_info: Person) -> None:
        cursor.execute("""INSERT INTO contacts (name, address, phone, id) 
        VALUES (?, ?, ?, ?)""", [new_contact_info.name,
                                 new_contact_info.address,
                                 new_contact_info.phone, new_contact_info.id])
        conn.commit()

    def delete_from_table(self, search_id_str: str) -> None:
        cursor.execute("DELETE FROM contacts WHERE id = ?", (search_id_str,))
        conn.commit()

    def update_table(self, new_contact_info: Person, contact_id: str) -> None:
        cursor.execute("""UPDATE contacts SET name = ?, address = ?, phone = ?, 
        id = ? WHERE id = ?""", [new_contact_info.name,
                                 new_contact_info.address,
                                 new_contact_info.phone, new_contact_info.id,
                                 contact_id])
        conn.commit()

    def get_all_contacts(self) -> List[Person]:
        cursor.execute("""SELECT * FROM contacts""")
        out_info = Person("", "", "", "")
        out_list = []
        tupl = cursor.fetchall()
        for i in range(len(tupl)):
            out_info.name = tupl[i][0]
            out_info.address = tupl[i][1]
            out_info.phone = tupl[i][2]
            out_info.id = tupl[i][3]
            out_list.append(out_info)
            out_info = Person("", "", "", "")
        return out_list

    def select_from_db(self, search_id_str: str) -> Person:
        sql = "SELECT * FROM contacts WHERE id=?"
        cursor.execute(sql, [search_id_str])
        tupl = cursor.fetchall()
        find_info = Person("", "", "", "")
        find_info.name = tupl[0][0]
        find_info.address = tupl[0][1]
        find_info.phone = tupl[0][2]
        find_info.id = tupl[0][3]
        return find_info

    def create_table(self) -> None:
        cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (name text, 
               address text, phone text, id text)""")


conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()
