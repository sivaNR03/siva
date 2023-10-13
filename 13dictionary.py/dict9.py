#Write a Python program to remove a key from a dictionary
dict= {'name':'siva','age':'29','city':'hyderabad'}
remove = 'age'
if remove in dict:
    del dict[remove]
else:
    print(f"the key '{remove}' does not exist in the dictionary.")
    
print("after removel:", dict)