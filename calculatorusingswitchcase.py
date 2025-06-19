num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
choice=int(input("Enter choice:"))
match choice:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        if num2!=0:
           print(num1/num2)
        else:
            print("Division error")
    case _:
        print("Invalid operation4")