n = int(input())
arr = [0] * 200  # 배열 크기를 넉넉하게 설정
x = 100  # 시작 위치를 배열 중앙으로 설정

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'R':
        for i in range(a):
            arr[x] += 1
            x += 1
    elif b == 'L':
        for i in range(a):
            arr[x] += 1
            x -= 1
    arr[x] += 1  # 마지막 위치에서도 증가

cnt = 0
for i in range(len(arr) - 1):
    if arr[i] >= 2 and arr[i + 1] >= 2:
        cnt += 1

print(cnt)