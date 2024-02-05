def rotate_array_elements(nums_list, rotation_count):
    length = len(nums_list)

    # Handle cases where rotation_count is greater than the array length
    rotation_count = rotation_count % length

    # Reverse the entire array
    nums_list.reverse()

    # Reverse the first rotation_count elements
    nums_list[:rotation_count] = reversed(nums_list[:rotation_count])

    # Reverse the remaining elements
    nums_list[rotation_count:] = reversed(nums_list[rotation_count:])


numbers_list = [1, 2, 3, 4, 5, 6]
rotation_count = 3

rotate_array_elements(numbers_list, rotation_count)
print(numbers_list)
