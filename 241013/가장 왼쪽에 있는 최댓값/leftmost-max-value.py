n = int(input())

arr = list(map(int, input().split()))

while True:
    if len(arr) == 1: 
        break
    if arr:
        num = max(arr)
    else:
        break
    for i in range(len(arr)):
        if arr[i] == num:
            if i == 0:
                print(1)
                arr = []
                break
            else:
                print(i+1, end=' ')
                arr = arr[:i]
                break