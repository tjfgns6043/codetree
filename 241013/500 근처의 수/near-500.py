arr = list(map(int, input().split()))

max_num = 1
min_num = 1000

for i in range(10):
    if arr[i] < 500 and arr[i] > max_num:
        max_num = arr[i]
    elif arr[i] > 500 and arr[i] < min_num:
        min_num = arr[i]
    else:
        continue
print(max_num, min_num)