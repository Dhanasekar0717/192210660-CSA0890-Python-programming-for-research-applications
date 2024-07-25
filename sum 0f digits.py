n = int(input("enter the number:"))
sum =0
temp=n
while temp>0:
    digit = temp % 10
    sum+= digit
    temp =temp//10
    print("sum of digit:",sum)
