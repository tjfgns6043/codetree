import sys
arr = list(map(int, input().split()))

max_value = -sys.maxsize

for i in range(len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
print(max_value)