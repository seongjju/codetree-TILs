n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
for i in arr:
    print(i,end=' ')
arr1=list(reversed(arr))
print()
for i in arr1:
    print(i,end= ' ')