"general way to find the common prefix"
Input: strs = ["flower","flow","flight"]
Output: "fl"

res=''
for i in range(len(strs[0])):
  for s in strs:
    if i==len(s) or s[i]!=strs[0][i]:
      return res
   res+=strs[0][i]
 return res


"optimized method using zip"
s=list(zip(*strs))  # zip(*chr) it which zips sub sequence characters
for i in s:
  if len(set(i))==1:
    res+=i[0]
  else:
    return res
return res
