#Custom Module with Aliases 
#Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, 
# capitalizing). In your main script, import this module using an alias and utilize its functions.
#Code Example:
    # text_utils.py
#    def reverse_string(s):
        # function to reverse a string
#    def capitalize_string(s):
        # function to capitalize a string
    # main.py
    # Import text_utils using an alias and utilize its functions

import text_utils as tu

while True:
    user_string = input("Enter a string (or type 'exit' to quit): ")
    if user_string.lower() == 'exit':
        break
        
    print("\nChoose an operation:")
    print("1. Reverse the string")
    print("2. Convert the string to uppercase")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
            result = tu.reverse_string(user_string)
            print(f"Reversed string: {result}")
    elif choice == '2':
            result = tu.capitalize_string(user_string)
            print(f"Uppercase string: {result}")
    else:
        print("Invalid choice. Please select 1 or 2.")
    print("-" * 40)


