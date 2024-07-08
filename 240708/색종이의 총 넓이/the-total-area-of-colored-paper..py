n = int(input())

arr = [ [0]* 201 for _ in range(201)]
cnt=0
for _ in range(n):
    x1,y1 = map(int,input().split())
    x2,y2 = 8+x1, 8+ y1
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] =1



for i in range(len(arr)):
    for j in arr[i]:
        if j==1:
            cnt+=1

print(cnt)