
#update
str = {'siva','raju'}
index =1
str.update({"naga"})
print(str)

# len,clear,
str =["s","i","v","a","n","a","g","a","r","a","j","u"]
print(len(str))
str.clear()
print(str)

# get
str ={'name':"siva",'emp':"56",'place':"kondapur"}
print(str.get('place'))
print(str.keys())
print(str.values())
print(str.items())
str.pop('place')
print(str)

#sample example get
a=input()
b=input()
c=input()
d=input()
d={a:b,b:c}
print(d)

#for loop
str ={'name':"siva",'emp':"56",'place':"kondapur"}
for i in str:
    print(i)