n=int(input())
arr = list(map(int, input().split()))

    
def f(x):
    maxs=0
    for i in arr:
        if i>maxs:
            maxs=i
    return maxs

print(f(n))