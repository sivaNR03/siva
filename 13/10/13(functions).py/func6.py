#6.write a function to find sum of given values, pass values has variable number of arguments to function.

def sum_values(*args):
    return sum(args)

result1 = sum_values(1, 2, 3, 4)
result2 = sum_values(5, 6, 7)
result3 = sum_values(8)
result4 = sum_values()

print("Sum of values (1, 2, 3, 4):", result1)
print("Sum of values (5, 6, 7):", result2)
print("Sum of a single value (8):", result3)
print("Sum of no values:", result4)
