n=int(input())    
arr=list(map(int,input().split()))
arr2=[-1] * n
arr[0] = arr2[0]
for j in range(1,n):
     arr2[j]=max(arr[j],arr2[j-1])

cnt=0
x=[]
for i in arr2:
    if i not in x:
        x.append(i)
        cnt+=1

print(cnt)