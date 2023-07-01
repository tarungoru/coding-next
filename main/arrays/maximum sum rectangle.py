
1
n,m=4,5
arr=[[1 2 -1 -4 -20],
[-8 -3  4 2 1],
[3  8 10 1 3],
[-4 -1 1 7 -6]]

# optimized code


max_sum = float('-inf')
for left in range(m):
  temp = [0] * n
  for right in range(left, m):
    for row in range(n):
      temp[row] += arr[row][right]
      curr_sum = 0
      max_temp_sum = float('-inf')
    for num in temp:
      curr_sum = max(num, curr_sum + num)
      max_temp_sum = max(max_temp_sum, curr_sum)
      max_sum = max(max_sum, max_temp_sum)
return max_sum
