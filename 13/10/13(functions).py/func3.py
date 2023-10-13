#Write a Python function to check whether a string is a pangram or not.
def pangram(input_string):
    alphabet=set()
    for char in input_string:
        if char.isalpha():
            alphabet.add(char.lower())
    return len(alphabet)==26

input_string = "the quick brown fox jumps over the lazy dog"
result= pangram(input_string)
if result:
    print("the input string is pangram.")  
else:
    print("the input string is not pangram ")           
    