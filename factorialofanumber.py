def factorial(num):
    if num<1:
        print("Error")
        return None
    elif num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("Enter a number:"))
result=factorial(num)
if result is not None:
    print(f"Factorial of {num} is {result}")
    