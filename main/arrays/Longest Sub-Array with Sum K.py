Input :
A[] = {10, 5, 2, 7, 1, 9}
K = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.

# Brute force solution

res=0
for i in range(len(arr)):
  sum=0
  for j in range(i,len(arr)):
    sum+=arr[j]
    if sum==k:
      res=max(res,j-i+1)
print(res)


# using hash map

res=0
sum=0
hash={}
for i,c in enumerate(arr):
  sum+=c
  if sum==k:
    res=max(res,i+1)
  rem=sum-k
  if rem in hash:
    res=max(res,i-hash[rem])
  if sum not in hash:
    hash[sum]=i
print(res)





