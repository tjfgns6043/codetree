n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = arr[0][0]
# 시작후 오른쪽이동 
for i in range(1,n): 
    dp[0][i] = dp[0][i-1] + arr[0][i]

# 시작 후 아래로 이동
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + arr[i][0]

# 점화식 dp[i][j] = max(arr[i][j] + dp[i][j-1], arr[i][j] + dp[i-1][j])

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(arr[i][j] + dp[i][j-1], arr[i][j] + dp[i-1][j])

print(dp[n-1][n-1])