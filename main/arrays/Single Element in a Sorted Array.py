You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.


Input: A = [1,1,2,3,3,4,4,8,8]
Output: 2


# Using Hash Map

hash={}
for i in range(len(A)):
  if A[i] in hash:
    hash[A[i]]+=1
  else:
    hash[A[i]]=1
for i in hash:
  if hash[i]==1:
    print(i)


# using binary search

l=0
r=len(A)-1
while l<=r:
  mid=(l+r)//2
  if (mid-1<0 or A[mid]!=A[mid-1]) and (mid+1==len(A) or A[mid]!=A[mid+1]):
    print(A[mid])
  left=mid-1 if A[mid]==A[mid-1] else mid
  if left%2:
    r=mid-1
  else:
    l=mid+1
