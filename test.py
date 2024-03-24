from collections import Counter
from heapq import heappush

s = "absdkjfklsjgklahfgjlhkglfhbjk"
c = Counter(s)
print(c)

h = []
for k, v in c.items():
    heappush(h, (-v, k))
    print(h[0][1], -h[0][0])