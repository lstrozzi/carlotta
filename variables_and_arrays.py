import random

def main():
    sentences = [
        "Have a great day!",
        "Keep up the good work!",
        "You are doing awesome!",
        "Stay positive and happy!",
        "Believe in yourself!"
    ]
    
    exit = False
    while not exit:
        print()
        print("=== Menu: ===")
        print("1. Greet")
        print("2. Show a number")
        print("3. Show a string")
        print("99. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            print(f"Hello, {name}!")
        elif choice == '2':
            number = random.randint(1, 100)
            print(f"Random number: {number}")
        elif choice == '3':
            sentence = random.choice(sentences)
            print(f"Random sentence: {sentence}")
        elif choice == '99':
            print("Goodbye!")
            exit = True
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
