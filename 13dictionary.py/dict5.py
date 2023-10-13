#Write a Python program to create a dictionary from a string.
def create_dict(input_string):
    letter_count = {}

    for char in input_string:
        if char.isalpha():
            char = char.lower() 
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

# Test the function with a sample string
sample_string = 'marolix technology'
result = create_dict(sample_string)

for letter, count in result.items():
    print(f"'{letter}': {count}")
