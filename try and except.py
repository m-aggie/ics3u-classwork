#Exercise 81
import math

def main():
    side1 = get_number("Enter the length of side a. \n")
    side2 = get_number("Enter the length of side b. \n")
    find_the_hypotenuse(side1, side2)

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print("Input Invalid")
    return number

def find_the_hypotenuse(side1, side2):
    hypotenuse = math.sqrt(side1**2 + side2**2)
    print(hypotenuse)

if __name__ == "__main__":
    main()

#Exercise 82
def main():
    while True:
        try:
            distance = float(input("Enter the distance travelled (km). "))
            if distance < 1:
                raise IndexError
            break
        except (ValueError,IndexError):
            print("Please enter a number. ")

    calculate_the_taxi_fare(distance)

def calculate_the_taxi_fare(distance):
    base_fare = 4.00
    additional_fare = 0.25*(distance/.14)
    total_fare = base_fare + additional_fare
    total_fare = round(total_fare,2)
    print(total_fare)

if __name__ == "__main__":
    main()
    
#Exercise 83
def main():
    while True:
        try: 
            items = int(input("Enter the number of items you want to ship. "))
            if items < 0:
                raise IndexError
            break
        except(ValueError, IndexError):
            print("Invalid. Enter another number. ")
    shipping_calculator(items)

def shipping_calculator(items):
    if items == 1:
        print("$10.95")
    if items > 1:
        total = 10.95 + (2.95*(items-1))
        total = round(total,2)
        print(total)

if __name__ == "__main__":
    main()
    
#Exercise 84 
def main():
    num1 = get_valid_number("Enter the first number. ")
    num2 = get_valid_number("Enter the second number. ")
    num3 = get_valid_number("Enter the third number. ")
    med = find_median(num1, num2, num3)
    print(med)

def get_valid_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Invalid number. ")
    return num

def find_median(num1, num2, num3):
    lowest = min(num1, num2, num3)
    highest = max(num1, num2, num3)
    total = sum([num1, num2, num3])
    median = total - highest - lowest
    return median

if __name__ == "__main__":
    main()

#Exercise 85
def main():
    while True:
        try:
            number = int(input("Enter a number. "))
            if number < 1 or number > 12:
                raise IndexError
            break
        except(ValueError, IndexError):
            print("Invalid number.")
    
    integer_to_ordinal_number(number)

def integer_to_ordinal_number(number):
    if number == 1:
        print("first")
    elif number == 2:
        print("second")
    elif number == 3:
        print("third")
    elif number == 4:
        print("fourth")
    elif number == 5:
        print("fifth")
    elif number == 6:
        print("sixth")
    elif number == 7:
        print("seventh")
    elif number == 8:
        print("eighth")
    elif number == 9:
        print("ninth")
    elif number == 10:
        print("tenth")
    elif number == 11:
        print("eleventh")
    elif number == 12:
        print("twelfth")

if __name__ == "__main__":
    main()
