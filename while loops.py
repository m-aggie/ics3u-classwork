#Exercise 1
while True:
 number = int(input("Enter a number: "))
 if number%2 == 0:
   print("Even")
 else:
   print("Odd")
   
#Exercise 2
while True:
 sides = int(input("Number of sides: "))
 if sides == 3:
   print("triangle")
 elif sides == 4:
   print("quadrilateral")
 elif sides == 5:
   print("pentagon")
 elif sides == 6:
   print("hexagon")
 elif sides == 7:
   print("heptagon")
 elif sides == 8:
   print("octagon")
 elif sides == 9:
   print("nonagon")
 elif sides == 10:
   print("decagon")
 else: 
    print("Shape does not exist")
    
#Exercise 3
 while True:
 month = input("Enter name of month: ").lower()
 if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december" :
   print("31 days")
 elif month == "february" :
   print("28 or 29 days")
 elif month == "april" or month == "june" or month == "september" or month == "november":
   print("30 days")
 else:
   print("month does not exist")
   
#Exercise 4
while True:
 denomination = int(input("Enter the amount of the banknote: "))
 if denomination == 1:
   print("George Washington is on your banknote")
 elif denomination == 2:
   print("Thomas Jefferson is on your banknote")
 elif denomination == 5:
   print("Abraham Lincoln is on your banknote")
 elif denomination == 10:
   print("Alexander Hamilton is on your banknote")
 elif denomination == 20:
   print("Andrew Jackson is on your banknote")
 elif denomination == 50:
   print("Ulysses S. Grant is on your banknote")
 elif denomination == 100:
   print("Benjamin Franklin is on your banknote")
 else:
   print("Invalid")
   
#Exercise 5
while True:
 month = input("Enter a month: ").lower()
 day = input("Enter a day: ")
 if month == "january" and day == "1":
   print("It is New Year's Day!")
 elif month == "july" and day == "1":
   print("It is Canada Day!")
 elif month == "december" and day == "25":
   print("It is Christmas!")
 else:
   print("Not a national holiday")
