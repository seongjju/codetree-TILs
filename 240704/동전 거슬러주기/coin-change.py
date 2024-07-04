n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [9999999] * (m + 1)
dp[0] = 0

for i in range(1, m + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[m] == 9999999:
    print(-1)
else:
    print(dp[m])