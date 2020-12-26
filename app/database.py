import sqlite3
from typing import List
from Person import Person


def insert_into_table(new_contact_info: Person):
    cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (name text, 
    address text, phone text, id text)""")
    cursor.execute("""INSERT INTO contacts (name, address, phone, id) 
    VALUES (?, ?, ?, ?)""", (new_contact_info.name, new_contact_info.address,
                             new_contact_info.phone, new_contact_info.id))
    conn.commit()


def delete_from_table(search_id_str: str):
    cursor.execute("DELETE FROM contacts WHERE id = ?", (search_id_str,))
    conn.commit()


def update_table(new_contact_info: Person, contact_id: str):
    cursor.execute("""UPDATE contacts SET name = ?, address = ?, phone = ?, 
    id = ? WHERE id = ?""", (new_contact_info.name, new_contact_info.address,
                             new_contact_info.phone, new_contact_info.id,
                             contact_id))
    conn.commit()


def load_sql_database() -> List[tuple]:
    cursor.execute("""SELECT * FROM contacts""")
    return cursor.fetchall()


def select_from_db(search_id_str: str) -> List[tuple]:
    sql = "SELECT * FROM contacts WHERE id=?"
    cursor.execute(sql, [search_id_str])
    return cursor.fetchall()


conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

