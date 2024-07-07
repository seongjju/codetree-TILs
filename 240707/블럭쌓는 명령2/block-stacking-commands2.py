a,b= map(int,input().split())
arr=[0]*(a+1)
for i in range(b):
    a1,a2=map(int,input().split())
    for i in range(a1,a2+1):
        arr[i]+=1

print(max(arr))