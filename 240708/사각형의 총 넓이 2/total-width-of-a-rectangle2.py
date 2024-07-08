n= int(input())
arr = [[0]*201 for _ in range(201)]
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1+1+100,x2+1+100):
        for j in range(y1+1+100,y2+1+100):
            arr[i][j]= 1

cnt=0
for i in range(len(arr)):
    for j in arr[i]:
        if j==1:
            cnt+=1

print(cnt)