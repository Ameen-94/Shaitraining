# Welcome message for the volunteer
print("Hello! Welcome to our volunteer program.")
print("Let's create your profile together!")

# Constants for emergency contacts --> Don't forget to write the constants in capital letters.
EMERGENCY_CONTACT = "911"  # Emergency contact number (constant)
ORGANIZATION_PHONE = "123-456-7890"  # Organization's main contact number (constant)

# Collecting volunteer's details
phone_number = input("Please enter your phone number: ")  # Volunteer phone number
age = int(input("Please enter your age: "))  # Volunteer age
academic_background = input("Please share your academic background: ")  # Academic background

# Availability details
availability = input("When are you available to volunteer? (Weekdays, Weekends, or Both): ")

# Displaying the profile
print("\nVolunteer Profile") # \n is used to insert a line break, which moves the cursor to the next line.
print(f"Phone Number: {phone_number}")
print(f"Age: {age}")
print(f"Academic Background: {academic_background}")
print(f"Availability: {availability}")