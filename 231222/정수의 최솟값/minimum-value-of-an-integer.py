re=0
def sums(a,b,c):
    re = min(a,b,c)
    return re
a,b,c=map(int,input().split())
print(sums(a,b,c))