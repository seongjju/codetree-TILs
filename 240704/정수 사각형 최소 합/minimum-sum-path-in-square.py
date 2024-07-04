n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

arr2=[[0]* n for _ in range(n)]
arr2[0][n-1] = arr[0][n-1]
for i in range(n-2,-1,-1):
    arr2[0][i]=arr[0][i]+arr2[0][i+1]
for i in range(1,n):
    arr2[i][n-1]=arr[i][n-1]+arr2[i-1][n-1]

for i in range(1,n):
    for j in range(n-2,-1,-1):
        arr2[i][j] = min(arr[i][j]+arr2[i-1][j], arr[i][j]+arr2[i][j+1])
print(arr2[n-1][0])