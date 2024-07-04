n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]


def fun(row_s,row_e, col_s, col_e):
    gold = 0
    for row in range(row_s,row_e+1):
        for col in range(col_s,col_e+1):
            gold +=arr[row][col]
    return gold

ans=0
for i in range(0,n-2):
    for j in range(0,n-2):
        ans=max(ans,fun(i,i+2,j,j+2))
print(ans)