#find sum of integers in the string
string_with_digit=input("string_digits: ")
count=0
for i in string_with_digit:
    if i.isdigit():
        count+=int(i)
print(count)        