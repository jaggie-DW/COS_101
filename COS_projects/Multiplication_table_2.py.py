Python 14.8 (tags/v3.14.8:e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
... def show_table(number):
...     """Print the multiplication table for one number."""
...     print(f"\nMultiplication table for {number}")
...     print("-" * 25)
...     for i in range(1, 13):
...         print(f"{number} x {i:2} = {number * i}")
... 
... 
... def show_full_grid():
...     """Print the whole 1-12 grid."""
...     print("\n     " + "".join(f"{n:5}" for n in range(1, 13)))
...     print("     " + "-" * 60)
...     for row in range(1, 13):
...         print(f"{row:3} |" + "".join(f"{row * col:5}" for col in range(1, 13)))
... 
... 
... def main():
...     print("=== Multiplication Table (1-12) ===")
... 
...     while True:
...         print("\nMenu:")
...         print("1. Show the table for one number")
...         print("2. Show the full 1-12 grid")
...         print("3. Quit")
... 
...         choice = input("Choose an option (1-3): ")
... 
...         if choice == "1":
...             try:
...                 number = int(input("Enter a number between 1 and 12: "))
...                 if 1 <= number <= 12:
...                     show_table(number)
...                 else:
...                     print("Please enter a number between 1 and 12.")
...             except ValueError:
                print("That's not a valid number. Try again.")

        elif choice == "2":
            show_full_grid()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


