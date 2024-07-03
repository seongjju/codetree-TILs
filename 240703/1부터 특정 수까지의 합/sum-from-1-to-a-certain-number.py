n=int(input())

def fun(n):
    sums=0

    for i in range(1,n+1):
        sums+=i
    return sums

print(fun(n)//10)