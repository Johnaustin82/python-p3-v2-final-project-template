from . import CONN, CURSOR

class InventoryItem:
    @classmethod
    def create_item(cls, name, description, price, quantity, reorder_level, supplier_id):
        CURSOR.execute('''
            INSERT INTO inventory_items (name, description, price, quantity, reorder_level, supplier_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, description, price, quantity, reorder_level, supplier_id))
        CONN.commit()
        return CURSOR.lastrowid
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('SELECT * FROM inventory_items WHERE id = ?', (id,))
        return CURSOR.fetchone()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM inventory_items')
        return CURSOR.fetchall()

    @classmethod
    def update_item(cls, id, name=None, description=None, price=None, quantity=None, reorder_level=None, supplier_id=None):
        query = 'UPDATE inventory_items SET '
        params = []
        if name:
            query += 'name = ?, '
            params.append(name)
        if description:
            query += 'description = ?, '
            params.append(description)
        if price:
            query += 'price = ?, '
            params.append(price)
        if quantity:
            query += 'quantity = ?, '
            params.append(quantity)
        if reorder_level:
            query += 'reorder_level = ?, '
            params.append(reorder_level)
        if supplier_id:
            query += 'supplier_id = ?, '
            params.append(supplier_id)
        query = query.rstrip(', ') + ' WHERE id = ?'
        params.append(id)
        CURSOR.execute(query, tuple(params))
        CONN.commit()
    
    @classmethod
    def delete_item(cls, id):
        CURSOR.execute('DELETE FROM inventory_items WHERE id = ?', (id,))
        CONN.commit()