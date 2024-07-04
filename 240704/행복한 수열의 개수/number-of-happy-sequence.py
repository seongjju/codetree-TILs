def count_happy_sequences(a, b, arr):
    cnt = 0

    # 행 검사
    for r in range(a):
        result = 1
        for c in range(1, a):
            if arr[r][c] == arr[r][c-1]:
                result += 1
            else:
                if result >= b:
                    cnt += 1
                result = 1
        if result >= b:
            cnt += 1

    # 열 검사
    for c in range(a):
        result = 1
        for r in range(1, a):
            if arr[r][c] == arr[r-1][c]:
                result += 1
            else:
                if result >= b:
                    cnt += 1
                result = 1
        if result >= b:
            cnt += 1

    return cnt

# 입력 받기
a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(a)]

# 결과 출력
re = count_happy_sequences(a, b, arr)
print(re)