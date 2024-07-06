#일 시 분
a,b,c = map(int,input().split())

#기준
sa,sb,sc = 11,11,11
# arr = [0,31,28,31,30,31,50,31,31,30,31,30,31]

cnt= 0

if a>=11 and b>= 11 and c>11:
    print(-1)

while True:
    if sa == a and sb == b and sc == c:
        break
        
    cnt +=1
    sc+=1

    if sc == 60:
        sc=0
        sb+=1
    if sb == 24:
        sb=0
        sa+=1

print(cnt)