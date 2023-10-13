#.Write a Python script to merge two Python dictionaries.

def merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1
	

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = merge(dict1, dict2)
print(dict3)
