arr = [ [0]* 201 for _ in range(201)]
cnt=0
n=int(input())
flag=0
for _ in range(n):
    if flag ==0:
        x1,y1,x2,y2 = map(int,input().split())
        x1 = x1 + 100
        y1 = y1 + 100
        x2 = x2 + 100
        y2 = y2 + 100
        flag+=1
        for i in range(x1,x2):
            for j in range(y1,y2):
                arr[i][j] = 1
    else:
        x1,y1,x2,y2 = map(int,input().split())
        x1 = x1 + 100
        y1 = y1 + 100
        x2 = x2 + 100
        y2 = y2 + 100
        flag-=1
        for i in range(x1,x2):
            for j in range(y1,y2):
                arr[i][j]  = 2



for i in range(len(arr)):
    for j in arr[i]:
        if j==2:
            cnt+=1

print(cnt)