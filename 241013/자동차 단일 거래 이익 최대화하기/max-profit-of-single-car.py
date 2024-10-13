n = int(input())

arr = list(map(int, input().split()))

price_min = min(arr)
price_max = max(arr)

if price_max - price_min == 0:
    print(0)
else:
    print(price_max - price_min)