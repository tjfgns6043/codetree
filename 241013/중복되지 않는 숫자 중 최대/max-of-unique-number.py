n = int(input())

arr = list(map(int, input().split()))

cnt = 0
max_value = 0
ok = False
for i in range(len(arr)):
    if cnt < 2 and arr[i] >= max_value:
        max_value = arr[i]
        cnt += 1
        ok = True
    else:
        cnt = 0
        ok = False
        continue
if ok:
    print(max_value)
else:
    print(-1)