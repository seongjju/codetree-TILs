n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

arr2=[[0]* n for _ in range(n)]
arr2[0][0] = arr[0][0]
for i in range(n):
    arr2[0][i]=arr[0][i]+arr2[0][i-1]
for i in range(n):
    arr2[i][0]=arr[i][0]+arr2[i-1][0]

for i in range(1,n):
    for j in range(1,n):
        arr2[i][j] = max(arr[i][j]+arr2[i-1][j], arr[i][j]+arr2[i][j-1])
print(arr2[n-1][n-1])