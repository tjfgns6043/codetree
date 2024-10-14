n, m = map(int, input().split()) 

arr = [list(map(int, input().split())) for _ in range(n)]

special = [[0 for _ in range(n)] for _ in range(n)]

movings = [list(map(int, input().split())) for _ in range(m)]

special[n-2][0], special[n-2][1] = 1, 1
special[n-1][0], special[n-1][1] = 1, 1

dxs = [0, -1, -1, -1, 0, 1, 1, 1] # 1-8 동쪽부터 반시계방향
dys = [1, 1, 0, -1, -1, -1, 0, 1]

growth = [(-1,1), (1,1), (1,-1), (-1,-1)] # 대각선

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

for i in range(m):
    # step1 특수 영양제를 이동 규칙에 따라 이동
    d, p = movings[i]
    d = d-1
    new_special = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if special[x][y] == 1:
                nx = (x + dxs[d]*p) % n
                ny = (y + dys[d]*p) % n
                new_special[nx][ny] = 2
    special = new_special
                    
    # step2 & 3 해당 땅에 특수 영양제를 투입하고 대각선 성장
    for x in range(n):
        for y in range(n):
            if special[x][y] == 2:
                special[x][y] = -1 # 영양제 투입 후 제거
                arr[x][y] += 1
                for dx, dy in growth: # 대각선
                    nx, ny = x + dx, y + dy
                    if in_range(nx,ny) and arr[nx][ny] >= 1:
                        arr[x][y] += 1
    
    # step4 특수 영양제 투입한 리브로수 제외 높이 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로스로 특수 영양제를 사고 해당 위치에 특수 영양제를 올려둡니다
    for x in range(n):
        for y in range(n):
            if special[x][y] == -1:
                special[x][y] = 0
            elif arr[x][y] >= 2:
                arr[x][y] -= 2
                special[x][y] = 1

# 최종 높이 출력
total = sum(sum(row) for row in arr)
print(total)