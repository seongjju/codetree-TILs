def minimize_movement(n, A, B):
    total_distance = 0
    excess_people = 0

    for i in range(n):
        excess_people += A[i] - B[i]
        total_distance += abs(excess_people)
    
    return total_distance

# 입력 예제
n = 4
A = [5, 4, 3, 1]
B = [3, 2, 3, 5]

print(minimize_movement(n, A, B))