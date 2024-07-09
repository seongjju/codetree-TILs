n=int(input())
arr=[0]*101
for _ in range(n):
    x1,x2= map(int,input().split())
    for i in range(x1,x2+1):
        arr[i]+=1

cnt=0


for i in arr:
    if i==n-1:
        cnt+=1

if cnt>=1:
    print("Yes")
else:
    print("No")