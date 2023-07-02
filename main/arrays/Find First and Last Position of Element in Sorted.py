Input: arr = [5,7,7,8,8,10], x = 8
Output: [3,4]

# using hash map

hash={}
temp=0
for i in range(len(arr)):
  if arr[i] not in hash:
    if arr[i]==x:
      hash[arr[i]]=i
      temp=i
    else:
      if arr[i]==x:
        hash[arr[i]]=i
  if x in hash:
    return [temp,hash[x]]
  else:
    return [-1,-1]

# using binary search


def searchRange(arr: [int], x: int) -> [int]:
    l=binary(arr,x,True)
    r=binary(arr,x,False)
    return [l,r]
def binary(arr,x,flag):
    left=0
    right=len(arr)-1
    i=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]>x:
            right=mid-1
        elif arr[mid]<x:
            left=mid+1
        else:
            i=mid
            if flag:
                right=mid-1
            else:
                left=mid+1
    return i
    
