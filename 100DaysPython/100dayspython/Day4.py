#import ใช้กับเวลามีหล่ายmoduleได้เช่น
#import Day1
#print(Day1.Yo)

# random function https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
import random
random_int= random.randint(1,20)
print(random_int)

random_float=random.uniform(1, 200)
print(random_float)

#List ใช้เก็บข้อมูลหลายตัว เริ่มด้วย[]เสมือ เช่น fruits=[item1,item2]
city_in_thailand=["Sukhothai Kingdom","Ayutthaya Kingdom","Thonburi Kingdom","Rattanakosin Kingdom"]
#ในคอมพิวเตอร์เริ่มนับตำเเหน่งจาก0เสมอ** ถ้าเป็น-1จะเริ่มนับจากท้ายสุด
print(city_in_thailand[0])
# Append=เพิ่มรายชื่อเดียวไปท้ายสุดในรายการ หรือ Extend เพิ่มหลายรายชื่อไปตอนท้าย https://docs.python.org/3/tutorial/datastructures.html


#To input user information into list by
usertype=input()
userlist=usertype.split()
n=int(len(userlist)) #ทำไมไม่ต้องลบ1เพราะปกติตัวเเรกนับจาก0?
#ใน range จะรวมตัวเเรกเเต่ไม่รวมตัวสุดท้าย สรุปคือ [0,n)
for x in range(0,n):
    userlist[x]=int(userlist[x])
print(userlist)

fruits=["Strawberries", "Spinach", "Kale", "Nectarines", "Apples" ,"Grapes" ,"Peaches", "Cherries"]
vegables=["Pears", "Tomatoes" ,"Celery", "Potatoes"]

dirty_dozen=[fruits,vegables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2]) # [] ตัวเเรก = listตำเเหน่งไหน , []ตัวหลัง = itemตำเเหน่งไหนในlistที่เราเลือกมา
print(dirty_dozen[1][3]) # [] ตัวเเรก = listตำเเหน่งไหน , []ตัวหลัง = itemตำเเหน่งไหนในlistที่เราเลือกมา

# .index ไว้ระบุต่ำเเหน่งในลิส
letter=input()
abc=["a","b","c"]
letterindex=abc.index(letter)
print(letterindex)

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
print(options[player])
computer=options[random.ranint(0,2)]
print(f"Computer choose:\n {computer}")

if (computer==0 and player==2) or (computer==1 and player==0) or (computer==2 and player==0):
    print("You lose")
elif computer==player:
    print("Draw!")
else:
    print("You win!!")
