def missing_positive(nums):
    nums_set=set(nums)
    smallest=1
    while smallest in nums_set:
        smallest+=1
    return smallest
nums=[1,3,-1,2]
print(missing_positive(nums))