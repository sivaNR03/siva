def add(num1:int,num2:int):
    """ add two numbers"""
    num3=num1+num2
    return num3
# drive code
num1=100
num2=43
num3=add(num1,num2)
print(num3)


# even numbers
def print_evennumbers(x):
    new_list=[]
    for i in  range(1,x):
        if i%2 == 0:
            new_list.append(i)
    print(new_list)
n=int(input("even numbers: "))            
print_evennumbers(n)

#even and odd numbers
def print_numbers(x,y):
    even=[]
    odd=[]
    for i in range(x,y+1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("even:",even)
    print("odd:",odd)      
x=int(input("enter x value:"))
y=int(input("enter y value:"))
print_numbers(x,y)      


#squares
def print_sqares(a):
    evens=[]
    odds=[]
    for i in range(a):
        if i % 2 ==0:
            evens.append(i)
    return evens
a=int(input("enter a value:"))  
z=print_sqares(a)
new=[]
for i in z:
    square =i*i
    new. append(square)
print(new)



  









        
       
         

 

    
