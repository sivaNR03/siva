#Remove Repeated Character from String
def remove_repeated_chars(string):
    return ".join(set(string))"


string ="hello"
result = remove_repeated_chars(string)
print(result)
        