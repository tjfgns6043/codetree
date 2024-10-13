arr = [list(map(int,input().split())) for _ in range(2)]

sum_row1 = sum(arr[0])
sum_row2 = sum(arr[1])

sum_col1 = arr[0][0] + arr[1][0]
sum_col2 = arr[0][1] + arr[1][1]
sum_col3 = arr[0][2] + arr[1][2]
sum_col4 = arr[0][3] + arr[1][3] 

len_row1 = len(arr[0])
len_row2 = len(arr[1])

len_col1= 2
len_col2 = 2
len_col3 = 2
len_col4 = 2

total = 0
for i in range(2):
    for j in range(4):
        total += arr[i][j]

print(f'{sum_row1/len_row1:.1f} {sum_row2/len_row2:.1f}')
print(f'{sum_col1/len_col1:.1f} {sum_col2/len_col2:.1f} {sum_col3/len_col3:.1f} {sum_col4/len_col4:.1f}')
print(f'{total/8:.1f}')