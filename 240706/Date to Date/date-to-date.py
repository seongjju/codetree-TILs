a,b,c,d = map(int,input().split())

arr = [0,31,28,31,30,31,50,31,31,30,31,30,31]

cnt= 0
while True:
    if a==c and b== d:
        break
        #일단 31일이 말일이라고 가정
    cnt +=1
    b+=1
    if b==arr[a]:
        a+=1 
        b=0
    
print(cnt+1)