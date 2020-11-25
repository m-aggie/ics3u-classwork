Python Workbook

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

#Exercise 6
side_1 = int(input("Enter the length of the first side: "))
side_2 = int(input("Enter the length of the second side: "))
side_3 = int(input("Enter the length of the third side: "))
if side_1 == side_2 == side_3:
  print("The triangle is an equilateral triangle")
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
  print("The triangle is an isosceles triangle")
else:
  print("The triangle is a scalene triangle")
  
#Exercise 7
C4_freq = 261.63
D4_freq = 293.66
E4_freq = 329.63
F4_freq = 349.23
G4_freq = 392.00
A4_freq = 440.00
B4_freq = 493.88
name = input("Enter the note: ")
note = name[0]
octave = int(name[1])
if note == "C":
  freq = C4_freq
elif note == "D":
  freq = D4_freq
elif note == "E":
  freq = E4_freq
elif note == "F":
  freq = F4_freq
elif note == "G":
  freq = G4_freq
elif note == "A":
  freq = A4_freq
freq = freq/2**(4-octave)
print(f"The frequency of {name} is {freq}")

#Exercise 8
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

#Exercise 9
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
  
#Exercise 10
column = input("Enter the letter of the column: ").lower()
row = int(input("Enter the row number: "))
if column == "a" or column == "c" or column == "e" or column == "g":
  if row%2 == 0:
    print("The square is white")
  else:
    print("The square is black")
elif column == "b" or column == "d" or column == "f" or column == "h":
  if row%2 == 0:
    print("The square is black")
  else:
    print("The square is white")
  
 Codingbat

#hello_name
def hello_name(name):
  return "Hello " + (name) + "!'"

#make_abba
def make_abba(a, b):
  return a + b + b + a

#make_tags
def make_tags(tag, word):
  return "<" +tag+ ">" + word +"</" +tag+ ">"

#make_out_words
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#extra_end
def extra_end(str):
  if len(str) <= 2:
    return str + str + str
  else:
    return str[-2:] +str[-2:] + str[-2:]
  
#first_two
def first_two(str):
  if len(str) <= 2:
    return (str)
  else:
    return str[:2]

#first_half
def first_half(str):
  return str[:len(str)/2]

#without_end
def without_end(str):
  return str[1:len(str)-1]

#combo_string
def combo_string(a, b):
  if len(a) < len(b):
    return a+b+a
  else: 
    return b+a+b
  
#non_start
def non_start(a, b):
  return a[1:len(a)-0] + b[1:len(b)-0]
