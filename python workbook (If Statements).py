#Exercise 1
number = int(input("Enter a number: "))
if number%2 == 0:
  print("Even")
else:
  print("Odd")
  
#Exercise 2
letter = input("Enter a letter: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
  print("vowel")
else: 
  print("consonent")

#Exercise 3
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
  
#Exercise 4
month = input("Enter name of month: ")
if month == "January" or month == "March" or month == "May" or month == "July" or month =="August" or month == "October" or month == "December" :
  print("31 days")
elif month == "February" :
  print("28 or 29 days")
else: 
  print("30 days")
  
#Exercise 5
decibel = int(input("Enter a decibel: "))
if decibel == 40:
  print("Quiet room")
elif decibel < 40:
  print("too quiet")
elif decibel > 40 and decibel < 70:
  print("Between quiet room and alarm clock")
elif decibel == 70:
  print("alarm clock")
elif decibel > 70 and decibel < 106:
  print("Between alarm clock and gas lawnmower")
elif decibel == 106:
  print("Gas lawnmower")
elif decibel > 106 and decibel < 130:
  print("Between gas lawnmower and jackhammer")
elif decibel == 130:
  print("jackhammer")
elif decibel > 130:
  print("too loud")
