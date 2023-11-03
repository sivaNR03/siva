# Define a function that concatenates a string to another string
def concatenate_string(s):
    return "Hello, " + s

# Create a list of strings
strings = ["Alice", "Bob", "Charlie", "David"]

# Use map to apply the concatenate_string function to each string in the list
result_strings = list(map(concatenate_string, strings))

# Print the original list and the result
print("Original Strings:", strings)
print("Resulting Strings:", result_strings)
