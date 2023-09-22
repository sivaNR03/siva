# count alphabets, digits, and special characters in the string

digits=1
alphabets=1
special_characters=1
given_string=input("enter_string:")
for i in given_string:
    if i.isdigit():
        digits+=2
    elif i.isalpha():
        alphabets+=2
    else:
        special_characters+=2

print(digits)
print(alphabets)
print(special_characters)