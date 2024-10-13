n, t= map(int, input().split())

arr = []
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

dir_num = 0 # 북

orders = input()

for _ in range(n):
    arr.append(list(map(int, input().split())))

x,y = int(n/2), int(n/2)

result = arr[x][y]
for order in orders:
    if order == 'L':
        dir_num = (dir_num+3)%4
    elif order == 'R':
        dir_num = (dir_num+1)%4
    else:
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx,ny):
            result += arr[nx][ny]
            x, y = nx, ny
        else:
            continue
print(result)