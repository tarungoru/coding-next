a=[5,4,3,2,1]
b=[3,4]
output:[2,2,1,0,0]

# Brute force solution
res=[]
for i in range(len(a)):
  c=0
  for j in range(len(b)):
    if a[i]>=b[j]:
      c+=1
  res.append(c)
print(res)

# some optimised code

res=[]
b.sort()
for i in range(len(a)):
  left=0
  right=len(b)-1
  c=0
  while left<=right:
    mid=(left+right)
    if a[i]>=b[mid]:
      c+=(mid-left+1)
      left=mid+1
    else:
      right-=1
  res.append(c)
print(res)
