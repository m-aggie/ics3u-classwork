#1
colour = input("What is your favourite colour? ")
print(f"{colour}! that is my favourite colour too")

#2
cans = int(input("How many cans come in the pack? "))
pack = int(input("How many packs are there? "))
total = cans*pack
print(f"The total number of cans is {total}")

#3
height = float(input("Enter the height: "))
width = float(input("Enter the width: "))
length = float(input("Enter the length: "))
volume = height*width*length
print(f"The volume is {volume}m3")

#4
user = str(input("Did you join the Google Meet and mute the teacher? "))
if user == "yes":
  print("That is probably not a good idea")
else: 
  print("Ok good")
