#replace string space with given character in Pytho
string="i am the king"
index=10
new_char='b'
new_string = string[:index]+new_char+string[index+1:]
print(new_string)