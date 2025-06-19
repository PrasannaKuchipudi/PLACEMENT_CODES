def even_pairs(arr):
    even=0
    odd=0
    for num in arr:
        if num%2==0:
            even+=1
        else:
            odd+=1
    even_pairs=(even*(even-1))//2
    odd_pairs=(odd*(odd-1))//2
    return even_pairs + odd_pairs
arr=[1,2,3,4]
print(even_pairs(arr))