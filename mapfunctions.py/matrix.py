#define a function that  multiplies a number by 2(matrix concept)
def square(x):
    return x ** 2
matrix=[
    [1,0,5,0],
    [0,1,5,0],
    [0,5,1,5],
    [0,5,0,1]
]
result=list(map(lambda row:list(map(square,row)),matrix))

print("matrix:")
for row in matrix:
    print (row)

print("matrix with each element square:")
for row in result:
    print (row)    


#same example i am using add
def add(n,m):
    return n + m

matrix1 =[
    [2,3,4,5],
    [1,1,1,1],
    [6,7,8,9],
]

matrix2 =[
    [6,7,8,9],
    [2,3,4,5],
    [1,3,5,6]

]
result_matrix=list(map(lambda row1,row2 :list(map(add , row1,row2)),matrix1,matrix2))

print("original matrix1:")
for row in matrix1:
    print(row)

print("original matrix2:")
for row in matrix2:
    print(row)

print("matrix add:")
for row in result_matrix:
    print (row)