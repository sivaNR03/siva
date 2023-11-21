     
            

def countOccur(char, string):
    count = 0
    for i in range(len(string)):
        if(string[i] == char):
            count = count + 1
    return count
string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = countOccur(char, string)
print("Total Number of occurence of ", char, "is :" , count) 
