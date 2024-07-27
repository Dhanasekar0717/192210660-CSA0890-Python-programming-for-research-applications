def weight(n):
    n = int(n, 2)
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
n = input("Enter the binary representation of integer: ")
result = weight(n)
print("The number of '1' bits is:", result)
