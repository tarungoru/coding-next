# using the optimised method

nums=[1,1,1,2,2,3]
k = 2
hash={}
for i in range(len(nums)):
    if nums[i] in hash:
        hash[nums[i]]+=1
    else:
        hash[nums[i]]=1
print(hash)
res=[[] for i in range(len(nums)+1)]
for i,c in hash.items():
    res[c].append(i)
fin=[]
for i in range(len(res)-1,-1,-1):
    if len(fin)==k:
        print(fin)
    while res[i]:
      fin.append(res[i].pop(0))
      
      
# using the heapq method
from collections import Counter
import heapq
heap=[]
s=Counter(nums)
for i,c in s.items():
  heapq.heappush(heap,(-c,i))
res=[]
for _ in range(k):
  res.append(heapq.heappop(heap)[1])
print(res)
  
