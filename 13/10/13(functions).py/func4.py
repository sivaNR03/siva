#4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
def print_sqares():
    squares=[]
    for i in range(1,10):
        if i % 2 ==0:
            squares.append(i**2)
    return squares
squares = print_sqares()
print(squares)

        