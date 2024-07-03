a,b=map(int,input().split())
cnts=0
for i in range(a,b+1):
    cnt=0
    for j in range(2,i):
        if i%j ==0:
            cnt+=1
            break
    if cnt==0:
        cnts+=i

print(cnts)