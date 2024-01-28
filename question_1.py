def remove_Duplicates(nums):

    n = len(nums)

    if n == 0 or n == 1:

        return n
    
    index = 0

    for i in range(1,n):
        if nums[i] != nums[index]:
            index += 1 
            nums[index] = nums[i]

    return index + 1 

numbers = [1,1,2,2,3]
print(remove_Duplicates(numbers))
