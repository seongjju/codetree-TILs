n=int(input())

arr=[]
while True:
    if n==1 or n==0:
        arr.append(n)
        break
    if n%2==1:
        arr.append(1)
        n=n//2
    else:
        arr.append(0)
        n=n//2

for i in arr[::-1]:
    print(i,end = '')