#Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.

cm = 2.54
inch = 1

while inch :
    if inch >=0:
        inch = int(input("enter the inch:"))
        con = cm*inch
        print(con)
    else:
        print("program end")
        break

