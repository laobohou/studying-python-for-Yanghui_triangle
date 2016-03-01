from functools import reduce
def f(a,b):
    return a*b
print(reduce(f, range(1, int(input('input a positive integar, then the factorial returns:\n'))+1)))
