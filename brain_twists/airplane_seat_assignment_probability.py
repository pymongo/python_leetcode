"""
由于只有第一个人不知道自己的座位号
除了第一个人，当第i个人选完座位后，第i个座上面一定有人，这样到最后只有第n个和第1个座位上存在不确定性
return 1 if n == 1 else 0.5

# dp[n]=(1+dp[2]+dp[3]+...+dp[n-1]+0)/n
dp = [0 for i in range(n+3)]
dp[1] = 1
dp[2] = 0.5
s = 1
# 1+dp[2]+dp[3]+...+dp[n-1]+0
for i in range(3,n+1):
    s += dp[i-1]
    dp[i] = s*1./i

return dp[n]
"""