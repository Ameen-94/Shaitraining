# Define the correct password (you can change this to any value you like)
correct_password = "secure123"  # This is the predefined correct password

# Prompt the user to input a password
user_password = input("Please enter your password: ")  # Ask the user for their password

# Check if the entered password matches the correct password
if user_password == correct_password:  # Conditional statement to compare the input with the correct password
    print("Welcome!")  # If the password is correct, display a welcome message
else:
    print("Did you forget your password?")  # If the password is incorrect, display an error message

# End of the program
print("Thank you for using our system!")  # Final message for the user
