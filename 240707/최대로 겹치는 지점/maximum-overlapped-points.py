n=int(input())
arr=[0]*200

for i in range(n):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        arr[i]+=1

    
print(max(arr))