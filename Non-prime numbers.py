a = int(input("Enter the starting value (a): "))
b = int(input("Enter the ending value (b): "))

for x in range(a+1, b + 1):
    if x > 1:
        is_prime = True
        for i in range(2, x):
            if (x % i) == 0:
                is_prime = False
                break
        if not is_prime:
            print(x)
