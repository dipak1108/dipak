#Write a program that asks for the biological gender and hemoglobin value (g/l).
#The program the notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

gender = str(input("Enter your gender (male/female): "))
hm = float(input("Enter the hemoglobin value (g/l): "))

if gender == "male":
    if  134 <= hm <=167:
        print("hemoglobin is normal")
    elif hm < 134 :
        print("hemoglobin is low")
    else :
        print("hemoglobin is high")

if gender == "female":
    if  117 <= hm <=155:
        print("hemoglobin is normal")
    elif hm < 117 :
        print("hemoglobin is low")
    else :
        print("hemoglobin is high")





