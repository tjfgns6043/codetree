n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dir_num = 0

len_alpha = len(alpha)
dx = [0, 1, 0, -1] # 동 남 서 북
dy = [1, 0, -1, 0]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

x, y = 0, 0
cnt = 1
arr[x][y] = 'A'
alpha_num = 1
while cnt < (n*m+1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if in_range(nx, ny) and arr[nx][ny] == 0:
        cnt += 1
        arr[nx][ny] = alpha[alpha_num]
        alpha_num = (alpha_num+1)%len_alpha
        x, y = nx, ny
    else:
        dir_num = (dir_num+1)%4

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()