n=int(input())
a=[0] * 1001
cnt=0
arr=[]
for i in range(n):
    a[i] = int(input())
    if i == 0 or a[i] == a[i - 1]:
        cnt += 1
    arr.append(cnt)
print(max(arr))