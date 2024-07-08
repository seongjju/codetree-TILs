arr = [ [0]* 2001 for _ in range(2001)]
cnt=0

for _ in range(1):
    x1,y1,x2,y2 = map(int,input().split())
    x1 = x1 + 1000
    y1 = y1 + 1000
    x2 = x2 + 1000
    y2 = y2 + 1000
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] =1


for _ in range(1):
    x1,y1,x2,y2 = map(int,input().split())
    x1 = x1 + 1000
    y1 = y1 + 1000
    x2 = x2 + 1000
    y2 = y2 + 1000
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] +=2


for i in range(len(arr)):
    for j in arr[i]:
        if j==1 or j==3:
            cnt+=1

x=0
for i in range(len(arr)):
    for j in arr[i]:
        if j==1 :
            x+=1
if x ==0: 
    print(x)
else:
    print(cnt)