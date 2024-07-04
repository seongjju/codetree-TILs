def count_beautiful_numbers(n, current_length=0):
    if current_length == n:
        return 1

    count = 0
    for i in range(1, 5):
        if current_length + i <= n:
            count += count_beautiful_numbers(n, current_length + i)
    
    return count

# 입력 받기
n = int(input())

# 결과 출력
print(count_beautiful_numbers(n))