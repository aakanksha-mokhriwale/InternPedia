print()
print("-----------------------------------------------------------------------------------------------------------------------------")
print("\t"*7, " ***CALCULATOR***")
print("-----------------------------------------------------------------------------------------------------------------------------") 
print()

#Choices of Operations to do for user
def options():
    print("Operations :")
    print("\t 1.Addition")
    print("\t 2.Subtraction")
    print("\t 3.Multiplication")
    print("\t 4.Division")
    print("\t 5.Exit")
    print()

def inputNo():
    num1=int(input("Enter First number:"))
    num2=int(input("Enter Second number:"))
    return num1, num2

def add(num1 , num2 ):
    return num1+num2;

def sub(num1 , num2 ):
    return num1-num2;

def mul(num1 , num2 ):
    return num1*num2;

def div(num1 , num2 ):
    if num2 == 0 :
        print(" Error !! Division by Zero not possible")
    else:
        return num1/num2;


Flag = True
while Flag == True:
    options()
    ch=int(input("Enter your choice (1-5) -- "))
    print()
    if ch==1:
        num1, num2 = inputNo()
        print("RESULT= " , add(num1,num2))
        print()
    elif ch==2:
        num1, num2 = inputNo()
        print("RESULT= " , sub(num1,num2))
        print()
    elif ch==3:
        num1, num2 = inputNo()
        print("RESULT= " , mul(num1,num2))
        print()
    elif ch==4:
        num1, num2 = inputNo()
        print("RESULT= " , div(num1,num2))
        print()
    elif ch==5:
        Flag = False

        print("Thank Youu !!")
    else:
        print("Wrong Input !! Try Again ...")
        print()

