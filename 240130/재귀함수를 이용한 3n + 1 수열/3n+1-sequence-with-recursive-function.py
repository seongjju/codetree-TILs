def f(x): 
    global cnt  # cnt 변수를 전역 변수로 선언
    if x == 1:
        return cnt
    if x % 2 == 0:
        x = x // 2
        cnt += 1
        return f(x)
    elif x % 2 != 0:
        x = (x * 3) + 1
        cnt += 1
        return f(x)

n = int(input())
cnt = 0  # cnt 변수 초기화
print(f(n))