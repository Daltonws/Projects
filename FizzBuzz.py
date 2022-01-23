#Write your code below this row 👇
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print (str(number) + 'is a multiple of 3 and 5')
#     elif number % 3 == 0:
#         print (str(number) + 'is a multiple of 3')
#     elif number % 5 == 0:
#         print (str(number) + 'is a multiple of 5')
#     else:
#         print (str(number))


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print ('FizzBuzz')
    elif number % 3 == 0:
        print ('Fizz')
    elif number % 5 == 0:
        print ('Buzz')
    else:
        print (str(number))
