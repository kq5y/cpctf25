n = int(input())
s = input()

# sに00もしくは0x0が含まれないようにする -> 0のindex差が3以上

# 条件を満たす最大の0の個数
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if s[i - 1] == "0":
        # 1にするか、0のまま維持するか
        dp[i] = max(dp[i - 1], dp[max(0, i - 3)] + 1)
    else:
        dp[i] = dp[i - 1]

print(s.count("0") - dp[n])
