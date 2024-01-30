a,b=map(int,input().split())

def cal(x,y):
    sums=0
    for n in range(x,y+1):
        cnt=0
        for i in range(2,n):
            if n%i==0:
                cnt+=1
        if cnt==0:
            sums+=n
    print(sums)

cal(a,b)