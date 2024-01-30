n=int(input())
def fact(x):
    sums=0
    for i in range(1,x+1):
        sums+=i
    print(sums)
fact(n)