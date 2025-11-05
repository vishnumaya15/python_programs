try: 
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    operator=input("enter operator '+','-','*','/'")

    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        result = num1/num2
    else:
        print('Enter valid operator')
    print(result)
except ValueError:
    print("Enter integer value")
except ZeroDivisionError:
    print("Cannot be divisible by 0")
except Exception as e:
    print("unexcepted error",e)