n = int(input())

arr = list(map(int, input().split()))

num = max(arr)
for i in range(n):
    if arr[i] == num:
        print(i, end=' ')