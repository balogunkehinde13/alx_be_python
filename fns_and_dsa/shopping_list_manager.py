shopping_list = []  # global list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    global shopping_list
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip() 
        
        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"✅ {item} added to your shopping list.")
        
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ {item} removed from your shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        
        elif choice == '3':
            if shopping_list:
                print("📝 Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
