# optimised approach

res=0
for i in grid:
  i.sort()
s=zip(*grid)
for i in s:
  res+=max(i)
print(res)

# brute force approach

for i in grid:
  i.sort()
res=0
for i in range(len(grid[0])-1,-1,-1):
  s=[]
  for j in range(len(grid)-1,-1,-1):
    s.append(grid[j][i])
    res+=max(s)
print(res)
