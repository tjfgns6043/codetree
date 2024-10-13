n = int(input())

arr = list(map(int, input().split()))

max_value = 0
ok = False
stack = []
for i in range(len(arr)):
    if i == len(arr) and max_value == 0:
        ok = False
    if arr[i] not in stack and arr[i] > max_value:
        max_value = arr[i]
        stack.append(arr[i])
        ok = True
        
if ok:
    print(max_value)
else:
    print(-1)