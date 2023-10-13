#5.Write a Python function to sum all the numbers in a list.
def sum_all_number(input_list):
    total=0
    for numbers in input_list:
        if isinstance(numbers,(int,float)):
         total += numbers
    return total
list=[8, 2, 3, 0, 7]
result=sum_all_number(list)
print("sum of numbers in the list:" ,result)


