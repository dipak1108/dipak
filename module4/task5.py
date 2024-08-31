#Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.

username = "python"
password = "rules"


i = 0
attempts = 0
while i < 5:

    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    if input_username == username and input_password == password:
        print("login successful")
        break
    else:
        attempts += 1
        if attempts < 5:
            print("login failed")
        else:
            print("access denied")
    i = i + 1
