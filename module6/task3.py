#Write a function that gets the quantity of gasoline in American gallons and returns the number converted
# to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def gallons_to_liters(gallons):
    return gallons * 3.78541  # 1 gallon = 3.78541 liters

def main():
    while True:
        gallons = float(input("Enter the quantity of gasoline in gallons: "))
        if gallons < 0:
            print("Negative value entered.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters:.2f} liters.")

if __name__ == "__main__":
    main()
