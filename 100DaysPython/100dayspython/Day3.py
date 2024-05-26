print("Welcome to the rollercoaster!")
adult=18
teenager=7
kid=5
phototic=3
height= int(input("What is your height in cm?\n"))
if height>=120:
    print("You good to go!!")
    age=int(input("What is your age?\n"))
    if 45<=age<=55:
        print("You can play this for free!!!")
    elif age>=18:
        print(f"You have to pay for adult price which is {adult}$")
        photo = input("Do you want to have extra photo for 3$? Yes/No?\n")
        if photo == "Yes"or"yes":
            print(f"Nice! you total bill is now {adult + phototic}$")
        else:
            print(f"Okay your total bill is {adult}$")
    elif 12<age<18:
        print(f"You have to pay for teenager price which is {teenager}$")
        photo = input("Do you want to have extra photo for 3$? Yes/No?\n")
        if photo == "Yes"or"yes":
            print(f"Nice! you total bill is now {teenager + phototic}$")
        else:
            print(f"Okay your total bill is {teenager}$")
    elif age<=12:
        print(f"You have to pay for kid price which is {kid}$")
        photo=input("Do you want to have extra photo for 3$? Yes/No?\n")
        if photo =="Yes"or"yes":
            print(f"Nice! you total bill is now {kid+phototic}$")
        else:
            print(f"Okay your total bill is {kid}$")
else:
    print("Sorry but you can't play this")

# ==คือEqual to, !=คือNot equal to
# % เอาไว้เช็คเศษ
#เวลาเรียงค่าเรียงจากน้อยไปมากก***
#not=นิเสธ

print("The Love Calculator is calculating your score...")
name1 = "Angela Yu" # What is your name?
name2 = "Jack Bauer" # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine=name1+name2
lowers=combine.lower()
t=lowers.count("t")
r=lowers.count("r")
u=lowers.count("u")
e=lowers.count("e")

l=lowers.count("l")
o=lowers.count("o")
v=lowers.count("v")
e=lowers.count("e")
firstscore=(t+r+u+e)
secondscore=(l+o+v+e)

total=float(str(firstscore)+str(secondscore))

if total<10 or total>90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif 40<total<50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")

#Final project
# '''ใช้สำหรับprintได้ เเละ\ด้วย** https://ascii.co.uk/art#google_vignette
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
decision1=input("'left' or  'right'\n").lower()
if decision1=="left":
    decision2=input("swim or wait?\n").lower()
    if decision2=="wait":
        decision3=input("You wait for a boat and arrived at island which door do want to choose?(Red, Blue, Yellow or any colors)\n").lower()
        if decision3 =="red":
            print("You got burned by fire game over:(")
        elif decision3=="blue":
            print("You got eaten by beasts game over :(")
        elif decision3=="Yellow"or"yellow":
            print("You found the treasure!!")
            print("Congratulation! you win!")
        else:
            print("Game over:(")


    else:
        print("You got attacked by trout game over:(")
else:
    print("You fall into a hole game over:(")





