def display(**m):
 print(m)
 for k,v in m.items():
    print(k,"-",v)
display(id1=100,id2=101,id3=102,id4=103)

#gloable variable
a=10
def f1():
    print(a)
def f2():
    print(a) 
print(a)
f1()
f2()

#local variable
a=10
def f1():
   
    print(a)
def f2():
    a=20
    print(a) 
print(a)
f1()
f2()


#gloable keyword
a=10
def f1():
    global a
    a=10
    print(a)
def f2():
    print(a) 
print(a)
f1()
f2()