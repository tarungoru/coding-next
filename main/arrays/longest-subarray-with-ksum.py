Input :
A[] = {10, 5, 2, 7, 1, 9}
K = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}

#brute force solution


res=0
i=0
sum=0
for j in range(len(arr)):
  sum+=arr[j]
  while sum>k:
    sum-=arr[i]
    i+=1
  if sum==k:
    res=max(j-i+1,res)
print(res)
