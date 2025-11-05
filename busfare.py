while True:
    name = input("Enter name or 'exit' to exit: ")
    if name.lower() == 'exit':
        print("Exiting")
        break
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Enter a  valid number")
        continue
    if age<5:
        print("Free,no fare")
        continue
    elif 5<=age<=10:
        print("Fare=10")
    elif 10 < age <= 20:
        print("Fare 20")
    elif 20<age<=30:
        print("Fare 30")
    elif 30 < age <=60:
        print("Fare 50")
    else :
        print("Free fare")