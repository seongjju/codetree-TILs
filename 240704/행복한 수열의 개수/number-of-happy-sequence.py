def count_happy_sequences(n, b, grid):
    happy_count = 0
    
    # 행 검사
    for r in range(n):
        current_length = 1
        for c in range(1, n):
            if grid[r][c] == grid[r][c-1]:
                current_length += 1
            else:
                if current_length >= b:
                    happy_count += 1
                current_length = 1
        if current_length >= b:
            happy_count += 1
    
    # 열 검사
    for c in range(n):
        current_length = 1
        for r in range(1, n):
            if grid[r][c] == grid[r-1][c]:
                current_length += 1
            else:
                if current_length >= b:
                    happy_count += 1
                current_length = 1
        if current_length >= b:
            happy_count += 1
    
    return happy_count

# 입력 받기
a, b = map(int, input().split())
arr = []
for _ in range(a):
    row = list(map(int, input().split()))
    arr.append(row)

# 결과 출력
result = count_happy_sequences(a, b, arr)
print(result)