num1=int(input("enter a number1: "))
operator=input("enter an operator '+','*','-','/'")
num2=int(input("Enter number 2: "))

if operator == '+':
    print (num1+num2)
elif operator =='-':
    print(num1-num2)
elif operator == '*':
    print (num1*num2)
elif operator=='/':
    if(num2!=0):
        result = num1/num2
        print (result)
    else:
        print("cannot be divided by 0")
else:
    print("enter valid operator")