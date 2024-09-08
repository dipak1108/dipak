#Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.


def sum_of_list(numbers):
    return sum(numbers)

def main():
    numbers = [3, 5, 7, 9, 11]
    total = sum_of_list(numbers)
    print(f"The sum of the list {numbers} is: {total}")

if __name__ == "__main__":
    main()
