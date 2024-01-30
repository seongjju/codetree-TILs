def f(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return f(x//3)+f(x-1)

n=int(input())
print(f(n))