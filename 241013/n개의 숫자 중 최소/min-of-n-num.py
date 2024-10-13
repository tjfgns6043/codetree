import sys

min_size = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] < min_size:
        min_size = arr[i]

print(min_size, arr.count(min_size))