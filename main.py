# Tyler Moon
# Week 9 - Assignment 9.1
# August 2, 2023

def get_user_data():
    # Asks the user for their name and stores it as the value name. Will only take alphabetic characters with an
    # if/else statement in a while loop to get the correct information from the user.
    while True:
        print("What is your name?")
        name = input()
        if name.isalpha():  # Check if the input consists only of alphabetic characters.
            break
        else:
            # Error message that prompts for correct input.
            print("Invalid input. Name should contain only alphabetic characters.")

    # Asks the user for their street name and stores it as the value streetName.
    print("What is your street name?")
    streetName = input()

    # Asks the user for their phone number and stores it as the value phoneNumber.
    # Will only take numbers with an if/else statement in a while loop to get the correct information from the user.
    while True:
        print("What is your phone number?")
        phoneNumber = input()
        if phoneNumber.isdigit():  # Check if the input consists only of numeric characters.
            break
        else:
            # Error message that prompts for correct input.
            print("Invalid input. Phone Number should contain only numbers.")
    # Returns variables to be called to the filename function by using the get_user_data function in filename function.
    return name, streetName, phoneNumber


def filename():
    # Asks the user for file name and stores it as the value fileName.
    print("What is your file name?")
    fileName = input()

    # Get the user data using the get_user_data function.
    name, streetName, phoneNumber = get_user_data()

    # Save the user data to a file with filename.
    with open(fileName, 'w') as file:
        # Write the user data to the file.
        file.write(f"Name: {name}")
        file.write(f"Street Name: {streetName}")
        file.write(f"Phone Number: {phoneNumber}")

    # Print the file with user data.
    print(f"File {fileName}: {name}, {streetName}, {phoneNumber}")


if __name__ == "__main__":
    filename()
