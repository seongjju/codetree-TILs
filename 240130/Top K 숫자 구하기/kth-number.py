n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr1=sorted(arr)
cnt=0
for i in arr1:
    cnt+=1
    if cnt==k:
        print(i)