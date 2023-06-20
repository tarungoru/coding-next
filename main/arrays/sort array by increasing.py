# native approach 

nums=[-1,1,-6,4,5,-6,1,4,1]
s={}
stack=[]
for i in range(len(nums)):
    s[nums[i]]=1+s.get(nums[i],0)
import heapq
heap=[]
arr=[]
for i in s:
    heapq.heappush(heap,[s[i],-i])
print(heap)
while heap:
    i,j=heapq.heappop(heap)
    arr.extend([-j]*i)
print(arr)

# if we sort array we do same like top nk elements
