import random

length=int(input("Enter the length of password :"))

lower="abcdefghigklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
symbols="!@#%$^&*()<>?.,"

char = lower+upper+num+symbols

passw=""

for i in range (length):
    passw+=random.choice(char)

print("Your Password is:" , passw)
