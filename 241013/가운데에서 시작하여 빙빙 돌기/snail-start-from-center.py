n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

dir_num = 0

dx = [0, -1, 0, 1] # 동 북 서 남
dy = [1, 0, -1, 0]

x, y = int(n/2), int(n/2)
arr[x][y] = 1

cnt = 1

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

while cnt < n**2:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if in_range(nx,ny) and arr[nx][ny] == 0:
        cnt += 1
        arr[nx][ny] = cnt
        x, y = nx, ny
    else:
        dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()