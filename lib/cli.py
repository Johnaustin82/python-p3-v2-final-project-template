# lib/cli.py

from helpers import (
    exit_program,
    create_shop,
    view_all_shops,
    update_shop,
    delete_shop,
    create_inventory_item,
    view_all_inventory_items,
    update_inventory_item,
    delete_inventory_item,
    create_supplier,
    view_all_suppliers,
    update_supplier,
    delete_supplier
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_shop()
        elif choice == "2":
            view_all_shops()
        elif choice == "3":
            update_shop()
        elif choice == "4":
            delete_shop()
        elif choice == "5":
            create_inventory_item()
        elif choice == "6":
            view_all_inventory_items()
        elif choice == "7":
            update_inventory_item()
        elif choice == "8":
            delete_inventory_item()
        elif choice == "9":
            create_supplier()
        elif choice == "10":
            view_all_suppliers()
        elif choice == "11":
            update_supplier()
        elif choice == "12":
            delete_supplier()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a new shop")
    print("2. View all shops")
    print("3. Update a shop")
    print("4. Delete a shop")
    print("5. Create a new inventory item")
    print("6. View all inventory items")
    print("7. Update an inventory item")
    print("8. Delete an inventory item")
    print("9. Create a new supplier")
    print("10. View all suppliers")
    print("11. Update a supplier")
    print("12. Delete a supplier")

if __name__ == "__main__":
    main()
