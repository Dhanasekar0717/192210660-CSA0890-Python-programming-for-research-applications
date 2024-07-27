def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
nums_input = input("Enter the sorted list of distinct integers separated by commas: ")
nums = [int(x) for x in nums_input.split(',')]
target = int(input("Enter the target value: "))
result = search_insert_position(nums, target)
print("Input: nums =", nums, ", target =", target)
print("Output:", result)
