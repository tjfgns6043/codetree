n = int(input())

arr = list(map(int, input().split()))

max_value = []

dp = [0 for _ in range(1001)]

for i in range(len(arr)):
    dp[arr[i]] += 1

for i in range(1,1001):
    if i == 1000 and dp[i] != 1:
        print(-1)
    if dp[i] == 1:
        print(i)
        break