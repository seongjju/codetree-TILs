def f(x):
    if x==1:
        return 2
    elif x==2:
        return 4
    else:
        return f(x-1)*f(x-2)

n=int(input())
print(f(n)%100)