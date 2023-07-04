Input : 
n = 4, k = 10
a[] = {1, 2, 3, 4}
Output : 
7
Explanation:
The contiguous subarrays are {1}, {2}, {3}, {4} 
{1, 2}, {1, 2, 3} and {2, 3} whose count is 7.


# brute force solution

res=0
for i in range(len(a)):
  pro=1
  for j in range(i,len(a)):
    pro*=a[j]
    if pro<k:
      res+=1
    else:
      break
print(res)


# optimal solution

res=0
pro=1
l=0
for i in range(len(a)):
  pro*=a[i]
  while l<len(a) and pro>=k:
    pro/=a[l]
    l+=1
  if pro<k:
    res+=(i-l+1)
print(res)
