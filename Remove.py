def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
nums_input = input("Enter the list of numbers separated by commas: ")
nums = [int(x) for x in nums_input.split(',')]
val = int(input("Enter the value to be removed: "))
k = remove_element(nums, val)
print("Output:", k, ", nums =", nums[:k] + [' '] * (len(nums) - k))
