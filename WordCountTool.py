print()
print("WELCOME TO WORD COUNT MACHINE  \n "  )

lCase="abcdefghigklmnopqrstuvwxyz"
uCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
symbols="!@#%$^&*()<>?.,"

uCount=0
lCount=0
nCount=0 
symCount=0
sCount=0


Flag = True

def WordCount(uCount , lCount , nCount , symCount , sCount):
    text=input("Enter your Text: ")
    for ch in text:
        if ch in lCase:
            lCount+=1
        elif ch in uCase:
            uCount+=1
        elif ch in num:
            nCount+=1
        elif ch in symbols:
            symCount+=1
        elif ch==" ":
            sCount+=1
        else:
            print("Invalid Charecter Found !! Cannot be counted !!")
    print()
    print("COUNT OF YOUR TEXT --")
    print("\t Lower Case Alphabets = " , lCount)
    print("\t Upper Case Alphabets = " , uCount)
    print("\t Symbols = " , symCount)
    print("\t Space = " , sCount)
    print("\t Numbers = " , nCount)
    print("\n")

#Accepting Text 
WordCount(uCount , lCount , nCount , symCount , sCount)

#Accepting Text while user wants to enter
while Flag == True:
    print("Do you want to enter more text , and know its word count ?")
    ans=input("Yes/No : ")
    if ans.upper() == "YES":
        WordCount(uCount , lCount , nCount , symCount , sCount)
        Flag = True
        print()
    else:
        print(" \n THANKS !! Come Again ")
        Flag = False


