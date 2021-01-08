#Exercise 81
import math

def find_the_hypotenuse(side1, side2):
    '''Finds the hypotenuse of a right-angle triangle

    Args:
        side1: the first side of the triangle
        side2: the second side of the triangle

    Returns:
        the lenght of the hypotenuse, rounded to 2 decimal places
    '''
    hypotenuse_squared = side1**2 + side2**2
    hypotenuse = math.sqrt(hypotenuse_squared)
    hypotenuse = round(hypotenuse,2)
    return hypotenuse 
    
#Test 
def test_find_the_hypotenuse():
    assert find_the_hypotenuse(3,4) == 5
    assert find_the_hypotenuse(4,5) == 6.4
    assert find_the_hypotenuse(9,10) == 13.45
    assert find_the_hypotenuse(6,8) == 10
    
#Exercise 82
def calculate_the_taxi_fare(distance):
    '''Finds the cost based on the distance travelled

    Args:
        distance: the distance travelled in km
    
    Returns:
        how much you owe to the taxi driver
    '''
    base_fare = 4.00
    additional_fare = 0.25*(distance/.14)
    total_fare = base_fare + additional_fare
    total_fare = round(total_fare,2)
    return total_fare
    
 #Test 
 def test_calculate_the_taxi_fare():
    assert calculate_the_taxi_fare(2) == 7.57
    assert calculate_the_taxi_fare(10) == 21.86
    assert calculate_the_taxi_fare(5) == 12.93
    assert calculate_the_taxi_fare(18) == 36.14
    
 #Exercise 83
 def shipping_calculator(items):
    '''Determines the cost of shipping based on the number of items

    Args:
        items: number of items you are shipping
    
    Returns:
        the cost of shipping
    '''
    if items == 1:
        return("10.95")
    if items > 1:
        total = 10.95 + (2.95*(items-1))
        total = round(total,2)
        return total
        
#Test
def test_shipping_calculator():
    assert shipping_calculator(2) == 13.9
    assert shipping_calculator(10) == 37.5
    assert shipping_calculator(25) == 81.75
    assert shipping_calculator(68) == 208.6
    
#Exercise 84
def find_median(num1, num2, num3):
    '''Finds the middle number

    Args: 
        num1 = the first number
        num2 = the second number
        num3 = the third number
    
    Returns:
        the middle number
    '''
    if num2 > num1 and num1 > num3:
        return(num1)
    elif num3 > num1 and num1 > num2:
        return(num1)
    elif num1 > num2 and num2 > num3:
        return(num2)
    elif num3 > num2 and num2 > num1:
        return(num2)
    elif num2 > num3 and num3 > num1:
        return(num3)
    elif num1 > num3 and num3 > num2:
        return(num3)
        
#Test
def test_find_median():
    assert find_median(3,4,5) == 4
    assert find_median(5,4,6) == 5
    assert find_median(10,9,11) == 10
    assert find_median(4,9,10) == 9
    
#Exercise 85
def integer_to_ordinal_number(number):
    '''Takes an integer and returns the ordinal number

    Args:
        number: an integer

    Returns:
        the ordinal number 
    '''
    if number == 1:
        return("first")
    elif number == 2:
        return("second")
    elif number == 3:
        return("third")
    elif number == 4:
        return("fourth")
    elif number == 5:
        return("fifth")
    elif number == 6:
        return("sixth")
    elif number == 7:
        return("seventh")
    elif number == 8:
        return("eighth")
    elif number == 9:
        return("ninth")
    elif number == 10:
        return("tenth")
    elif number == 11:
        return("eleventh")
    elif number == 12:
        return("twelfth")
        
#Test
def test_integer_to_ordinal_number():
    assert integer_to_ordinal_number(1) == "first"
    assert integer_to_ordinal_number(3) == "third"
    assert integer_to_ordinal_number(5) == "fifth"
    assert integer_to_ordinal_number(12) == "twelfth"
