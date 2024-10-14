n, m = map(int, input().split()) 

arr =[list(map(int, input().split())) for _ in range(n)]

special = [[0 for _ in range(n)] for _ in range(n)]

movings = [list(map(int, input().split())) for _ in range(m)]

special[n-2][0], special[n-2][1] = 1, 1
special[n-1][0], special[n-1][1] = 1, 1

dxs = [0, -1, -1, -1, 0, 1, 1, 1] # 1-8 동쪽부터 반시계방향
dys = [1, 1, 0, -1, -1, -1, 0, 1]

growth = [(-1,1), (1,1), (1,-1), (-1,-1)] # 대각선

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(m):
    # step1 특수 영양제를 이동 규칙에 따라 이동
    d, p = movings[i]
    d = d-1
    for x in range(n):
        for y in range(n):
            if special[x][y] == 1:
                special[x][y] = 0
                nx = x + dxs[d]*p
                ny = y + dys[d]*p
                if in_range(nx,ny):
                    special[nx][ny] = 2
                else:
                    if nx >= 0 and ny > n: # 오른쪽으로 벗어났을때
                        ny = ny%n
                    elif nx > n and ny >= 0: # 아래쪽으로 벗어났을때
                        nx = nx%n
                    elif nx >= 0 and ny < 0 : # 왼쪽으로 벗어났을때
                        ny = ny+min(n, 10)
                    elif nx < 0 and ny >= 0: # 위쪽으로 벗어났을떄
                        nx = nx+min(n, 10)
                    elif nx < 0 and ny > n: # 우측위 벗어났을떄
                        nx = nx+min(n, 10)
                        ny = ny%n
                    elif nx < 0 and ny < 0: # 좌측위 벗어났을떄
                        nx = nx+min(n, 10)
                        ny = ny+min(n, 10)
                    elif nx > n and ny > n: # 우측아래 벗어났을떄
                        nx = nx%n
                        ny = ny%n
                    elif nx > n and ny < 0: # 좌측아래 벗어났을떄
                        nx = nx%n
                        ny = ny+min(n, 10)
                    special[nx][ny] = 2
                    
    # step2 해당 땅에 특수 영양제를 투입하고. 투입 후 투입된 특수 영양제는 사라집니다
    # step3 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1이상인 리브로수가 있는 만큼 높이가 더 성장
    for x in range(n):
        for y in range(n):
            if special[x][y] == 2:
                special[x][y] = -1 # 영양제 투입 후 제거
                arr[x][y] += 1
                for dx, dy in growth: # 대각선
                    nx = x + dx
                    ny = y + dy
                    if in_range(nx,ny):
                        if arr[nx][ny] >= 1:
                            arr[x][y] += 1
    # step4 특수 영양제 투입한 리브로수 제외 높이 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로스로 특수 영양제를 사고 해당 위치에 특수 영양제를 올려둡니다
    for x in range(n):
        for y in range(n):
            if special[x][y] == -1:
                special[x][y] = 0
                continue
            else:
                if arr[x][y] >= 2:
                    arr[x][y] -= 2
                    special[x][y] = 1
total = 0
# 최종 높이 출력
for i in range(n):
    for j in range(n):
        total += arr[i][j]
print(total)