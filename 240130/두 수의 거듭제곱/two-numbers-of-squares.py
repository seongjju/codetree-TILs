a,b=map(int,input().split())

def pulse(x,y):
    x1=x
    for _ in range(y-1):
        x*=x1
    print(x)
pulse(a,b)