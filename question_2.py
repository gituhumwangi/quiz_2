def rotate_array(nums, k):
    n = len(nums)

    # Handle cases where k is greater than the array length
    k = k % n

    # Reverse the entire array
    nums.reverse()

    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # Reverse the remaining elements
    nums[k:] = reversed(nums[k:])


numbers = [1,2,3,4,5,6]
k = 3

print(rotate_array(numbers, k))