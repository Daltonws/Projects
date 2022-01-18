print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
# user ==  0
Left = int(0)
Right = int(1)
selection_1 = (input("You have walked deep into the Hollow Forest and need to get out! Would you like to go RIGHT or LEFT?\n")).lower() 
if selection_1 ==  "left":
   print("You have successfully found the exit of the forest now you but are being chased by Bandits looking to keep you hostage!!! You may continue on your quest!\n")
   selection_2 = (input("You have come across a river that you must cross. Would you like to wait for the boat or swim?")).lower()
   if selection_2 == "wait":
        selection_3 = input("You have crossed the river successfully safely and have reached an island. You have found a house with 3 doors. One red, one yellow and one blue. Which color door do you open? \n").lower()
        if selection_3 == "red":
          print("You have fallen into a pit of lava. Game Over.")
        elif selection_3 == "yellow":
            print("You found the treasure! You Win!")
        elif selection_3 == "blue":
          print("You have been swept away into the ragging ocean. Game Over.")
        else: 
          print("You made it this far and have chosen a door that is not an option. A bolder has crushed you!!! Game over!!!")
else:
  print("Game Over!")
