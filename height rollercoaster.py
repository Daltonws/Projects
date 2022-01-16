print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You are tall enough to ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age >= 18:
   print("You are over 18. Please pay 12 dollars")
  else:
    print("You are under 18. Please pay 7 dollars)
else:
  print("Sorry, you are NOT tall enough to ride the rollercoaster!")
