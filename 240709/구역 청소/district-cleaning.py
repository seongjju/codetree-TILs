a,b=map(int,input().split())
c,d=map(int,input().split())

sums=0
maxs=0
maxs = max(a,b,c,d)
mins = min(a,b,c,d)

sums = maxs-mins
print(sums)