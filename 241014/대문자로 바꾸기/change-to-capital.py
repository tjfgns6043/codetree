arr = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(3):
        arr[i][j] = arr[i][j].upper()
        print(arr[i][j], end=' ')
    print()