n = int(input())

arr = list(map(int, input().split()))

cnt = 0
max_value = 0
for i in range(len(arr)):
    if cnt < 2 and arr[i] >= max_value:
        max_value = arr[i]
        cnt += 1
    else:
        cnt = 0
        continue
print(max_value)