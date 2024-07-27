def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) / 2
    actual_sum = sum(nums)
    return int(expected_sum - actual_sum)
nums = list(map(int, input("Enter the integers separated by commas: ").split(',')))
result = missing_number(nums)
print("The missing number is:", result)
