def f(x):
    if x<10:
        return x*x
    else:
        return f(x//10)+(x%10)*(x%10)
n=int(input())
print(f(n))