import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

def initialize_db():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS shops (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS supplier (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact_person TEXT NOT NULL,
            contact_email TEXT NOT NULL,
            contact_phone TEXT NOT NULL
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS inventory_items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            quantity in kilo INTEGER NOT NULL,
            reorder_level INTEGER NOT NULL,
            supplier_id INTEGER NOT NULL,
            FOREIGN KEY (supplier_id) REFERENCES supplier(id)
        )
    ''')
    CURSOR.commit()


