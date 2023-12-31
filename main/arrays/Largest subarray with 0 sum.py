Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

# brute force code

res=0
for i in range(len(arr)):
  sum=0
  for j in range(i,len(arr)):
    sum+=arr[j]
    if sum==0:
      res=max(res,j-i+1)
print(res)

# optimized code using hash map

hash={}
res=0
sum=0
for i in range(len(nums)):
  sum+=nums[i]
  if sum==0:
    res=max(res,i+1)
  if sum in hash:
    res=max(res,i-hash[sum])
  else:
    hash[sum]=i
print(res)
