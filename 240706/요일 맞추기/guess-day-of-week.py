a,b,c,d = map(int,input().split())

arr = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
cnt= 0
#5월 4일 기준
#5월 5일
#6월 3일
#6월 5일
if (a<c) or (a==c and b<=d):

    while True:
        if a==c and b== d:
            break
        cnt +=1
        b+=1
        if b==arr[a]:
            a+=1 
            b=0
    print(day[cnt%7 + 1])

else:
    while True:
        if a==c and b== d:
            break
        cnt +=1
        d+=1
        if d==arr[c]:
            c+=1 
            d=0    
    print(day[cnt%7 - 1])