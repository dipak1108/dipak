#Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user
# to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for
# the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to
# each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

airports = {}
while True:
    print("\nOptions:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        icao_code = input("Enter ICAO code of the new airport: ").strip().upper()
        airport_name = input("Enter name of the airport: ").strip()
        airports[icao_code] = airport_name
        print(f"Airport '{airport_name}' with ICAO code '{icao_code}' has been added.")

    elif choice == '2':
        icao_code = input("Enter ICAO code of the airport to fetch: ").strip().upper()
        if icao_code in airports:
            print(f"Airport with ICAO code '{icao_code}' is '{airports[icao_code]}'.")
        else:
            print(f"No airport found with ICAO code '{icao_code}'.")

    elif choice == '3':
        print("Quitting the program.")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")