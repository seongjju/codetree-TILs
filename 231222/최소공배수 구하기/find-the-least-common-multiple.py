a,b = map(int,input().split())
lists=[]
for i in range(1+max(a,b),a*b):
    if i%a == 0 and i%b ==0:
        lists.append(i)

re = INF
for result in lists:
    if re>result:
        re = result
print(re)