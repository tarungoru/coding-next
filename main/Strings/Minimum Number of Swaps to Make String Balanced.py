# Minimum Number of Swaps to Make String Balanced

Input: s = "]]][[["
Output: 2

# using stack
stack = []
s = list(s)
for i in range(len(s)):
    if s[i] == '[':
        stack.append(i)
    if s[i] == ']' and len(stack) != 0:
        s[i] = ""
        c = stack.pop()
        s[c] = ""
    s1 = "".join(s)
left=0
right=len(s1)-1
c=0
while left<right:
    c+=1
    left+=2
    right-=2
print(c)

# using normal method


maxcount=0
res=0
for i in range(len(s)):
  if s[i]=='[':
    res-=1
  else:
    res+=1
  maxcount=max(maxcount,res)
print((maxcount+1)//2)
