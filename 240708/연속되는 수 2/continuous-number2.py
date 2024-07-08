n=int(input())
a=[0] * 1001
cnt=0
for i in range(n):
    a[i] = int(input())
    if i == 0 or a[i] != a[i - 1]:
        cnt += 1

print(cnt)