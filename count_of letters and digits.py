def count_letters_and_digits (input_string):
 letters = 0
 digits = 0
 for char in input_string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
 return letters , digits
input_string = input("enter a string:")
letters,digits = count_letters_and_digits (input_string)
print(f"no.of letters:{letters}")
print(f"no.of digits:{digits}")
        
            
