#2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct_element(input_list):
    distinct_list=list(set(input_list))
    return distinct_list


input_list =[1,2,3,4,5,3,2,6,7,7,8]
distinct_element = distinct_element(input_list)
print("Distinct elements:",distinct_element)
