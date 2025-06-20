def gcd_by_subtraction(num1,num2):
    while num1!=num2:
        if num1>num2:
            num1=num1-num2
        else:
            num2=num2-num1
    return num1
num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
result=gcd_by_subtraction(num1,num2)
print(f"The GCD of {num1} and {num2} is {result}")