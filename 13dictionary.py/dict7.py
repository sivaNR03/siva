#7.Write a Python program to combine two dictionary by adding values for common keys.
def combine_dic(d1,d2):
    combined_dict=d1.copy()
    for key ,value in d2.items():
        if key in combined_dict:
            combined_dict[key]+= value
        else:
            combined_dict[key] = value
    return combined_dict
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

result =combine_dic(d1,d2)
print("counter:" ,result)
