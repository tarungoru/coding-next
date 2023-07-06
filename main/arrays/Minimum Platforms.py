# optimial solution

Input: n = 6 
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation: 
Minimum 3 platforms are required to 
safely arrive and depart all trains.

arr.sort()
dep.sort()
plat=1
res=1
i=1
j=0
while i<len(arr) and j<len(arr):
  if dep[j]>=arr[i]:
    plat+=1
    i+=1
  elif(arr[i]>dep[j]):
    plat-=1
    j+=1
    res=max(res,plat)
print(res)
