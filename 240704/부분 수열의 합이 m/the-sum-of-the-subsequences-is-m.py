n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [9999999] * (m + 1)
dp[0] = 0

for num in arr:
    for j in range(m, 0, -1):
        if dp[j - num] != 9999999:  
            dp[j] = min(dp[j], dp[j - num] + 1)


if dp[m] == 9999999:
    print(-1)
else:
    print(dp[m])