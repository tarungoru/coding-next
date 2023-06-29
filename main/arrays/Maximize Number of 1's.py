Input:
N = 11
arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
M = 2
Output:
8
Explanation:
Maximum subarray is of size 8
which can be made subarray of all 1 after
flipping two zeros to 1.


# brute force code

res=0
i=0
zeros=0
for j in range(len(arr)):
  if arr[j]==0:
    zeros+=1
  while zeros>m:
    if arr[i]==0:
      zeros-=1
    i+=1
  res=max(res,j-i+1)
print(res)

# using sliding window technique

l=0
zeros=0
for r in range(len(arr)):
  if arr[r]==0:
    zeros+=1
  if zeros>m:
    if arr[l]==0:
      zeros-=1
    l+=1
return r-l+1

# Efficient solution
l=0
zeros=0
for r in arr:
  if not r:
    zeros+=1
  if zeros>m:
    if not arr[l]:
      zeros-=1
  l+=1
return len(arr)-l


