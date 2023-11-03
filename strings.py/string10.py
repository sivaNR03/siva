#check string is anagrams or not in Python
def check(s1, s2):
     
    
    s1 =input()
    s2 =input()
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings arent anagrams.")      





