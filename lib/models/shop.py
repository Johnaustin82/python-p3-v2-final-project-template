from . import CONN, CURSOR

class Shop:
    @classmethod
    def create_shop(cls, name, email, phone, address):
        CURSOR.execute('''
            INSERT INTO shops (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        ''', (name, email, phone, address))
        CONN.commit()
        return CURSOR.lastrowid
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('SELECT * FROM shops WHERE id = ?', (id,))
        return CURSOR.fetchone()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM shops')
        return CURSOR.fetchall()

    @classmethod
    def update_shop(cls, id, name=None, email=None, phone=None, address=None):
        query = 'UPDATE shops SET '
        params = []
        if name:
            query += 'name = ?, '
            params.append(name)
        if email:
            query += 'email = ?, '
            params.append(email)
        if phone:
            query += 'phone = ?, '
            params.append(phone)
        if address:
            query += 'address = ?, '
            params.append(address)
        query = query.rstrip(', ') + ' WHERE id = ?'
        params.append(id)
        CURSOR.execute(query, tuple(params))
        CONN.commit()
    
    @classmethod
    def delete_shop(cls, id):
        CURSOR.execute('DELETE FROM shops WHERE id = ?', (id,))
        CONN.commit()