# lib/helpers.py

from models.shop import Shop
from models.item import InventoryItem
from models.supplier import Supplier

def create_shop():
    name = input("Enter shop name: ")
    email = input("Enter shop email: ")
    phone = input("Enter shop phone: ")
    address = input("Enter shop address: ")
    shop_id = Shop.create_shop(name, email, phone, address)
    print(f"Shop created with ID: {shop_id}")

def view_all_shops():
    shops = Shop.get_all()
    for shop in shops:
        print(shop)

def create_inventory_item():
    name = input("Enter item name: ")
    description = input("Enter item description: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    reorder_level = int(input("Enter item reorder level: "))
    supplier_id = int(input("Enter supplier ID: "))
    item_id = InventoryItem.create_item(name, description, price, quantity, reorder_level, supplier_id)
    print(f"Inventory item created with ID: {item_id}")

def view_all_inventory_items():
    items = InventoryItem.get_all()
    for item in items:
        print(item)

def create_shop():
    name = input("Enter shop name: ")
    email = input("Enter shop email: ")
    phone = input("Enter shop phone: ")
    address = input("Enter shop address: ")
    shop_id = Shop.create_shop(name, email, phone, address)
    print(f"Shop created with ID: {shop_id}")

def view_all_shops():
    shops = Shop.get_all()
    for shop in shops:
        print(shop)

def update_shop():
    shop_id = int(input("Enter shop ID to update: "))
    shop = Shop.find_by_id(shop_id)
    if shop:
        name = input(f"Enter new name ({shop[1]}): ") or shop[1]
        email = input(f"Enter new email ({shop[2]}): ") or shop[2]
        phone = input(f"Enter new phone ({shop[3]}): ") or shop[3]
        address = input(f"Enter new address ({shop[4]}): ") or shop[4]
        Shop.update_shop(shop_id, name, email, phone, address)
        print("Shop updated successfully")
    else:
        print("Shop not found")

def delete_shop():
    shop_id = int(input("Enter shop ID to delete: "))
    shop = Shop.find_by_id(shop_id)
    if shop:
        Shop.delete_shop(shop_id)
        print("Shop deleted successfully")
    else:
        print("Shop not found")


def create_inventory_item():
    name = input("Enter item name: ")
    description = input("Enter item description: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    reorder_level = int(input("Enter item reorder level: "))
    supplier_id = int(input("Enter supplier ID: "))
    item_id = InventoryItem.create_item(name, description, price, quantity, reorder_level, supplier_id)
    print(f"Inventory item created with ID: {item_id}")

def view_all_inventory_items():
    items = InventoryItem.get_all()
    for item in items:
        print(item)

def update_inventory_item():
    item_id = int(input("Enter item ID to update: "))
    item = InventoryItem.find_by_id(item_id)
    if item:
        name = input(f"Enter new name ({item[1]}): ") or item[1]
        description = input(f"Enter new description ({item[2]}): ") or item[2]
        price = float(input(f"Enter new price ({item[3]}): ") or item[3])
        quantity  = int(input(f"Enter new quantity ({item[4]}): ") or item[4])
        reorder_level = int(input(f"Enter new reorder level ({item[5]}): ") or item[5])
        supplier_id = int(input(f"Enter new supplier ID ({item[6]}): ") or item[6])
        InventoryItem.update_item(item_id, name, description, price, quantity, reorder_level, supplier_id)
        print("Inventory item updated successfully")
    else:
        print("Inventory item not found")

def delete_inventory_item():
    item_id = int(input("Enter item ID to delete: "))
    item = InventoryItem.find_by_id(item_id)
    if item:
        InventoryItem.delete_item(item_id)
        print("Inventory item deleted successfully")
    else:
        print("Inventory item not found")

def create_supplier():
    name = input("Enter supplier name: ")
    contact_person = input("Enter contact person: ")
    contact_email = input("Enter contact email: ")
    contact_phone = input("Enter contact phone: ")
    supplier_id = Supplier.create_supplier(name, contact_person, contact_email, contact_phone)
    print(f"Supplier created with ID: {supplier_id}")

def view_all_suppliers():
    suppliers = Supplier.get_all()
    for supplier in suppliers:
        print(supplier)

def update_supplier():
    supplier_id = int(input("Enter supplier ID to update: "))
    supplier = Supplier.find_by_id(supplier_id)
    if supplier:
        name = input(f"Enter new name ({supplier[1]}): ") or supplier[1]
        contact_person = input(f"Enter new contact person ({supplier[2]}): ") or supplier[2]
        contact_email = input(f"Enter new contact email ({supplier[3]}): ") or supplier[3]
        contact_phone = input(f"Enter new contact phone ({supplier[4]}): ") or supplier[4]
        Supplier.update_supplier(supplier_id, name, contact_person, contact_email, contact_phone)
        print("Supplier updated successfully")
    else:
        print("Supplier not found")

def delete_supplier():
    supplier_id = int(input("Enter supplier ID to delete: "))
    supplier = Supplier.find_by_id(supplier_id)
    if supplier:
        Supplier.delete_supplier(supplier_id)
        print("Supplier deleted successfully")
    else:
        print("Supplier not found")

def exit_program():
    print("Goodbye!")
    exit()

