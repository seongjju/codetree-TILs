n=int(input())
arr=[0]*100

for i in range(n):
    a,b = map(int,input().split())
    for i in range(a,b):
        arr[i+100]+=1

    
print(max(arr))