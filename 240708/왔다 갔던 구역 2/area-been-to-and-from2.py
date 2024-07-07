n = int(input())
arr = [0] * 200
x = 100  # 초기 위치

for i in range(n):
    a, b = input().split()
    a = int(a)
    
    if b == 'R':
        for j in range(x + 1, x + a + 1):
            arr[j] += 1
        x += a  # 오른쪽으로 이동한 만큼 x 업데이트

    if b == 'L':
        for j in range(x - 1, x - a - 1, -1):
            arr[j] += 1
        x -= a  # 왼쪽으로 이동한 만큼 x 업데이트

cnt = 0
for i in range(len(arr) - 1):
    if arr[i] >= 2 and arr[i + 1] >= 2:
        cnt += 1

print(cnt)