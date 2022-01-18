import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list_of_names = (len(names))
random_name = random.randint(0, list_of_names - 1)
bill_payer = names[random_name]
print(f"{bill_payer} is going to buy the meal today!")
