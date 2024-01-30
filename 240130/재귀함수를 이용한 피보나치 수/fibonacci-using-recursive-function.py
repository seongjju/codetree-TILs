def f(n):
    # 종료 조건
    if n < 3:
        return 1

    # 재귀 호출
    return f(n - 1) + f(n - 2)

x=int(input())
print(f(x))