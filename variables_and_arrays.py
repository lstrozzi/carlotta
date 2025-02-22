def main():
    exit = False
    while not exit:
        print()
        print("=== Menu: ===")
        print("1. Greet")
        print("99. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            print(f"Hello, {name}!")
        elif choice == '99':
            print("Goodbye!")
            exit = True
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
