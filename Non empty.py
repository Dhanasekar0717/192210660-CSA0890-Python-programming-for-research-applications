def single_number(nums):
    unique = 0
    for num in nums:
        unique ^= num
    return unique
nums = list(map(int, input("Enter the integers separated by commas: ").split(',')))
result = single_number(nums)
print("The single number is:", result)
