print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#need to use lower case for names to support better calculations
name1 = str(name1.lower())
name2 = str(name2.lower())
#Need a catination here to create a single string of name char
combined_names = name1 + name2
#need to establish lower cases for static value "true love"
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e
# You str unable to conduct equations or conditions on 2 different data type as seen on line # 29 so we need to turn the string into int.
rating = int(str(first_digit) + str(second_digit))

if (rating < 10) or (rating > 90):
  print(f"Your rating is {rating}, you go together like coke and mentos.")
elif (rating >= 40) and (rating <= 50):
  print(f"Your rating is {rating}, you are alright together.")
else:
  print(f"Your rating is {rating}.")
