import sys

arr = list(map(int, input().split()))

max_value = -sys.maxsize
min_value = sys.maxsize

for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        break
    if arr[i] > max_value:
        max_value = arr[i]
    if arr[i] < min_value:
        min_value = arr[i]
print(max_value, min_value)