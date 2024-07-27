string1=input("enter the string:")
string2=input("enter the string:")
length=min(len(string1),len(string2))
count=0
for i in range(length):
    if string1[i]==string2[i]:
        count+=1
print(count)
