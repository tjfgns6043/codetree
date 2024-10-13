n = int(input())

arr = list(map(int, input().split()))

min_num = 100
for i in range(n-1):
    if abs(arr[i]-arr[i+1]) < min_num:
        min_num = abs(arr[i]-arr[i+1])
print(min_num)