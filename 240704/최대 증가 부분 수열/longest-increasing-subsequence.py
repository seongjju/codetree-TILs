n=int(input())    
arr=list(map(int,input().split()))
arr2=  [[-1]*n for _ in range(n)]
arr2[0][0] = arr[0]

for i in range(0,n):
    for j in range(i,n):
        arr2[i][j]=max(arr[j],arr2[i][j-1])

li=[]
for i in range(0,n):
    cnt=0
    x=[]
    for j in range(0,n):
        if arr2[i][j] != -1 and arr2[i][j] not in x:
            x.append(arr2[i][j])
            cnt+=1
    li.append(cnt)
print(max(li))