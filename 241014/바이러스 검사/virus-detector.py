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
        cnt += people // checks[1]
        people = people % checks[1]
        if people > 0:
            cnt += 1
print(cnt)