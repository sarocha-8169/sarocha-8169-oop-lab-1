import functools

def squareNum(n):
    return n**2

numLst = []
number = int(input("Enter an integer:"))
for i in range(1, number+1):
    numLst.append(i)
result = functools.reduce(lambda a, b: a + b, map(squareNum, numLst))
print(f'The sum of the square of {numLst} is {result}')