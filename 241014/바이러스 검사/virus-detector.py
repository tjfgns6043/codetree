n = int(input())
peoples = list(map(int, input().split()))
checks = list(map(int, input().split()))

cnt = 0
for people in peoples:
    if people <= checks[0]:
        cnt += 1
    else:
        cnt += 1
        people -= checks[0]
        if people // checks[1] == 0:
            cnt += 1
        else:
            cnt += people // checks[0] + 1
print(cnt)