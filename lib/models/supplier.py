from . import CONN, CURSOR

class Supplier:
    @classmethod
    def create_supplier(cls, name, contact_person, contact_email, contact_phone):
        CURSOR.execute('''
            INSERT INTO supplier (name, contact_person, contact_email, contact_phone)
            VALUES (?, ?, ?, ?)
        ''', (name, contact_person, contact_email, contact_phone))
        CONN.commit()
        return CURSOR.lastrowid
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('SELECT * FROM supplier WHERE id = ?', (id,))
        return CURSOR.fetchone()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM supplier')
        return CURSOR.fetchall()

    @classmethod
    def update_supplier(cls, id, name=None, contact_person=None, contact_email=None, contact_phone=None):
        query_parts = []
        params = []
        if name:
            query_parts.append('name = ?')
            params.append(name)
        if contact_person:
            query_parts.append('contact_person = ?')
            params.append(contact_person)
        if contact_email:
            query_parts.append('contact_email = ?')
            params.append(contact_email)
        if contact_phone:
            query_parts.append('contact_phone = ?')
            params.append(contact_phone)
        
        if query_parts:  
            query = 'UPDATE supplier SET ' + ', '.join(query_parts) + ' WHERE id = ?'
            params.append(id)
            CURSOR.execute(query, tuple(params))
            CONN.commit()
    
    @classmethod
    def delete_supplier(cls, id):
        CURSOR.execute('DELETE FROM supplier WHERE id = ?', (id,))
        CONN.commit()
        