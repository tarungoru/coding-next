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
