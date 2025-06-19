def rat_house(r,unit,arr):
    food_required=r*unit
    food=0
    for i in range(len(arr)):
        food+=arr[i]
        if food_required>food:
            return i+1
    return -1
r=7
unit=2
arr=[2,3,5,7,9,11,13]
print(rat_house(r,unit,arr))