n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

dir_num = 0

dx = [1, 0, -1, 0] # 하 우 상 좌
dy = [0, 1, 0, -1]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

x, y = 0, 0
arr[x][y] = 1
num = 1
while num < n*m:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        num += 1
        arr[nx][ny] = num
        x = nx
        y = ny
    else:
        dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()