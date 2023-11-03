#python program to demonstrate working  of map
def add(x):
    return x + x
numbers=[2,3,4,5,6]
result=list(map(add,numbers))
print(result)

#add 2 lists using map and lambda
list1=[5,6,7]
list2=[7,8,9]
result=map(lambda x,y: x + y,list1,list2)
print(list(result))