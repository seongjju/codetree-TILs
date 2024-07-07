n = int(input())
arr = [0] * 200  # 배열 크기를 넉넉하게 설정
x = 100  # 시작 위치를 배열 중앙으로 설정

# 명령을 처리하며 이동 경로 기록
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

cnt = 0
# 2번 이상 지나간 위치를 세기
for i in range(len(arr)):
    if arr[i] >= 2:
        cnt += 1

print(cnt)