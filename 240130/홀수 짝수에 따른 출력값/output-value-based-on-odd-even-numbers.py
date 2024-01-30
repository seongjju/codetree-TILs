def f(x):

    if x%2 ==0:
        if x==2:
            return 2
        return f(x-2)+x
    else:
        if x==1:
            return 1
        else:
            return f(x-2)+x

n=int(input())
print(f(n))