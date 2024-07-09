a,b=map(int,input().split())
c,d=map(int,input().split())
im1=0
im2=0
if a>c:
    im1=c
    c=a
    a=im1
    im2=b
    b=d
    d=im2

sums=0
maxs=0
maxs = max(a,b,c,d)
mins = min(a,b,c,d)

if b<c:
    sums = b-a + d-c

else:
    sums = maxs-mins
print(sums)