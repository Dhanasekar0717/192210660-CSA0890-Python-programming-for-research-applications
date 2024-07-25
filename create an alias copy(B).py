a = [1, 2, 3, 4, 5]
b = a
print("Initial state of a:", a)
print("Initial state of b (alias of a):", b)
a[2] = 99
print("\nAfter modification:")
print("State of a:", a)
print("State of b (alias of a):", b)
b.append(6)
b.append(7)
print("\nAfter another modification:")
print("State of a:", a)
print("State of b (alias of a):", b)
