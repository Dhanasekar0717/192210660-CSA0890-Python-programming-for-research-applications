def is_palindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    return normalized_str == normalized_str[::-1]
s = input("Enter the string: ")
result = is_palindrome(s)
print(result)
