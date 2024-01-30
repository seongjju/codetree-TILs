n=int(input())
arr=list(map(int,input().split()))

arr.sort()

maxs=0
x=len(arr) //2

for i in range(0,x):
    maxs=max(arr[0+i]+arr[-1-i],maxs)
print(maxs)