x1,x2,x3,x4 = map(int,input().split())
arr=[0]*100
for i in range(x1,x2+1):
    arr[i]+=1
for i in range(x3,x4+1):
    arr[i]+=1

cnt=0

for i in arr:
    if i==2:
        cnt+=1

if cnt==0:
    print("nonintersecting")
else:
    print("intersecting")