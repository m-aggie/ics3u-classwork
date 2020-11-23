print("You are alone in a house.")
key = False
lights = False

while True:
  print()
  print("What do you do.")
  print("[1] explore")
  print("[2] exit")
  choice = input("> ")
  if choice == "1":
    print("You find the switch and turn on the lights.")
    print()
    print("Do you want to conitnue looking around?")
    choice = input("> ")
    if choice == "yes":
      print("You found the key")
      key = True
      print()
    else:
      print() 
      print("What do you do.")
      print("[1] explore")
      print("[2] exit")
      choice = input("> ")
  elif choice == "2":
    if key == True:
      print("You escaped yay!")
      break
    else:
      print("You need the key")
