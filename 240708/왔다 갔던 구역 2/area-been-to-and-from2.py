n=int(input())
arr=[0]*200
x=0
x=100 #현재
# arr[100] =1
for i in range(n):
    a,b = input().split()
    a=int(a)
    if b =='R':
        for i in range(x+1,a+x+2):
            arr[x] +=1
            x+=1
        x-=1
    if b == 'L':
        for i in range(x,a+x+1):
            arr[x] +=1
            x-=1     
        x+=1 
cnt=0
for i in range(len(arr)):
    if arr[i]>=2 and arr[i+1]>=2:
        cnt+=1
print(cnt)