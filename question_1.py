def remove_duplicates_from_list(nums_list):

    length = len(nums_list)

    if length == 0 or length == 1:
        return length
    
    new_index = 0

    for i in range(1, length):
        if nums_list[i] != nums_list[new_index]:
            new_index += 1 
            nums_list[new_index] = nums_list[i]

    return new_index + 1 

numbers_list = [1, 1, 2, 2, 3]
print(remove_duplicates_from_list(numbers_list))
