def recursive_function(x):
     if x == 1:
         return 1
     else:
         return x* recursive_function(x-1)  
num=5
print( recursive_function(num))


s=lambda n :n**2
m=s(9)
print(m)




