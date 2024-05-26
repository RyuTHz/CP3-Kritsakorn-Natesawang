#Final project
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
options=[rock,paper,scissors]
player=int(input("Type 0 for rock 1 for paper and 2 for scissors\n"))
print("This what you choose")
print(options[player])
x=random.randint(0,2)
computer=options[x]
print(f"Computer choose:\n {computer}")
computer=x

if player==0 and computer==2:
    print("You win!!!")
elif computer>player:
    print("You lose!")
elif player==computer:
    print("Draw!!")

