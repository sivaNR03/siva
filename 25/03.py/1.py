str = "i have a dog"
print(str.replace("dog", " "))



str = "i have a dog"
rm_string =input("enter a word to remove: ")
print(str.replace(rm_string, " "))


str = "i have a dog"
str1=" "
for s in str.split():
   if s == "dog":
    continue
    str1  += s+' '
print(str1)
  