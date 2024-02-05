def find_single_number(nums_list):
    result_value = 0
    for num in nums_list:
        result_value ^= num
    return result_value

numbers_list = [1, 2, 3, 4, 3, 2, 1]  # Example list with a single number occurring only once
print(find_single_number(numbers_list))
