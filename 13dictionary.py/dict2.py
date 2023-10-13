#2.Write a Python script to check whether a given key already exists in a dictionary.
dict= {'name':'siva','age':'29','city':'hyderabad'}
key_to_check ='age'
if dict.get(key_to_check) is not None:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")