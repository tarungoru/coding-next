"""You are given a list of lists, inner lists are neighbourhoods and have equal number of houses.
{{8,4,8}, {6,5,3}, {4,7,4}}
Then we are given another input which represents the color of these houses
{{y,u,o}, {y,h.p}, {t,u,i}}
Now we need to arrange the houses in such a manner that one neighborhood doesn't have a duplicate house number, color can be repeated.

o/p
{{3p,4u,7u},{4t,5h,8y},{4i,6y,8o}}
output should be in ascending order."""

from typing import *
from collections import *

class Rearrange:
    def arrange(self, neigh: List[List[int]], colors: List[List[str]]) -> List[List[str]]:
        R, C = len(neigh), len(neigh[0])
        d, ans = defaultdict(list), [[] for _ in range(R)]
        for nb, clr in zip(neigh, colors):
            for h, c in zip(nb, clr):
                d[h].append(c)
                if len(d[h]) > C:
                    return []
        i = 0
        for h, clr in d.items():
            for c in clr:
                ans[i % C].append(str(h) + c)
                i += 1
        print(ans)
        for l in ans:
            l.sort()
        return ans
ra = Rearrange()
neigh = [[8,4,8], [6,5,3], [4,7,4]]    
colors = [["y","u","o"], ["y","h","p"], ["t","u","i"]]
expectedAnswer = [["3p","4u","7u"],["4t","5h","8y"],["4i","6y","8o"]]
print(f'output = {ra.arrange(neigh, colors)}')
print(f'expectedAnswer = {expectedAnswer}')
neigh = [[8,4,8], [6,5,3], [4,7,4]]
colors = [["y","u","y"], ["y","h","p"], ["t","u","i"]]
print(f'output = {ra.arrange(neigh, colors)}')
neigh = [[8,8,8], [8,5,3], [4,7,4]]
print(f'output = {ra.arrange(neigh, colors)}')
