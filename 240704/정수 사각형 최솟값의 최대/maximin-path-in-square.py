n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

arr2=[[0]* n for _ in range(n)]
arr2[0][0] = arr[0][0]
for i in range(1,n):
    arr2[0][i]=arr[0][i]
for i in range(1,n):
    arr2[i][0]=arr[i][0]

for i in range(1,n):
    for j in range(1,n):
        arr2[i][j] = min(max(arr2[i-1][j],arr2[i][j-1]) , arr[i][j])
print(arr2[n-1][n-1])