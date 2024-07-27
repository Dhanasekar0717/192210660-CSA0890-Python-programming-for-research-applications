def length_of_last_word(s):
    s = s.strip()
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length
s = input("Enter a string consisting of words and spaces: ")
result = length_of_last_word(s)
print("Input: s =", s)
print("Output:", result)
