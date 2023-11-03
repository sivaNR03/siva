#remove character from string
s=input()
for i in s:
    if i.isalpha():
        r=(s.replace(i,""))
        s=r
    print(s)



