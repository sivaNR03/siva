#1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
def lower_upper(input_string):
    upper_count =0
    lower_count=0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count , lower_count

input_string="The quick Brow Fox"
upper_count ,lower_count = lower_upper(input_string)
print("upper letters:",upper_count)
print("lower letters:",lower_count)

        

