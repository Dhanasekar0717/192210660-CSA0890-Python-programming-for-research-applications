def count_bits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    
    return ans
n = int(input("Enter the integer n: "))
result = count_bits(n-1)
print("The array of 1's count is:", result)
