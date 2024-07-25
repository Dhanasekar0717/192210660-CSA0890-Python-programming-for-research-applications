num = int(input("enter the string:"))
a = 0
b = 1
c = 0
for i in range (2,num):
  c = (a+b)
  a = b
  b = c
print(c)
