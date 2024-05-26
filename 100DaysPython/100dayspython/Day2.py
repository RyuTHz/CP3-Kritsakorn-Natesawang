print(6 + 4 / 2 - (1 * 2))
# Programmers count from zero***
print("Hello"[4])
# ,ลูกน้ำเเทนด้วย_ในpython

num=str(len(input()))
print(num,"Char")

print(70+float("100.5"))
# **=ยกกำลัง
#PEMDAS
#()
#**
#* /
#+ -
#left to right
print(3*(3+3)/3-3)

#วิธีปัดเศษส่วนใช้ round or need int for divide use //
print(round(10/3,3))

# += -= *= /= is calculate previous data in variables

#print(f"Your score is {your variables}") : f-string is auto convert data type

#Final project
print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $ \n"))
tip_in=float(input("How much tip would oyu like to give? 10, 12, 15 or else in % \n"))/100*total_bill
people=float(input("How many people to spilt the bill ? \n"))
shared_amount=round(float((total_bill+tip_in)/people))
shared_amount_in_2_deci="{:.2f}".format(shared_amount)
print(f"Each person should pay: ${shared_amount_in_2_deci}")



