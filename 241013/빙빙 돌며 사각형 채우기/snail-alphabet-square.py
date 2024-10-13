n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

dir_num = 0

dx = [0, 1, 0, -1] # 동 남 서 북
dy = [1, 0, -1, 0]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

x, y = 0, 0
cnt = 1
arr[x][y] = 'A'

while cnt < n*m:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if in_range(nx, ny) and arr[nx][ny] == 0:
        if arr[x][y] == 'Z':
            cnt += 1
            arr[nx][ny] = 'A'
            x, y = nx, ny
        else:
            cnt += 1
            arr[nx][ny] = chr(ord(arr[x][y])+1)
            x, y = nx, ny
    else:
        dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()