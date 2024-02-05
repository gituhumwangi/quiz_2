def has_duplicates(nums_list):
    seen_set = set()
    for num in nums_list:
        if num in seen_set:
            return True
        seen_set.add(num)
    return False

numbers_list = [1, 2, 3, 4, 5, 6, 1]  # Example list with duplicates
print(has_duplicates(numbers_list))
