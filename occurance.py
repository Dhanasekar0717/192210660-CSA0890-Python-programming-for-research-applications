def str_str(haystack, needle):
    return haystack.find(needle)
haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")
index = str_str(haystack, needle)
print("Input: haystack = '{}', needle = '{}'".format(haystack, needle))
print("Output:", index)
