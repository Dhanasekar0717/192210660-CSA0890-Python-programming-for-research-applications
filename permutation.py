import itertools
def get_permutations(nums):
    return list(itertools.permutations(nums))
input_array = list(map(int, input("Enter the numbers: ").split()))
permutations = get_permutations(input_array)
for perm in permutations:
    print(perm)
