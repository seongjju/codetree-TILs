n=int(input())

def f(x):
    if x<2:
        return 1
    
    return f(x-1)*x
print(f(n))