n = int(input())

arr = list(map(int, input().split()))

margin = 0

for i in range(n): 
    for j in range(i+1, n):
        if(arr[j] - arr[i]) > margin:
            margin = (arr[j]-arr[i])
if margin == 0:
    print(0)
else:
    print(margin)