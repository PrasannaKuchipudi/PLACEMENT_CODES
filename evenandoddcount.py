start=int(input("Enter start range:"))
end=int(input("Enter end range:"))
even=0
odd=0
for i in range(start,end+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd",odd)