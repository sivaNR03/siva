# # .Write a Python program to access dictionary key's element by index.
my_dict = {0: 'physics', 1: 'math', 2: 'chemistry'}

keys_list = list(my_dict.keys())
index = 1
if index < len(keys_list):
    key = keys_list[index]
    value = my_dict[key]
    print(value)
else:
    print("Index out of range")
