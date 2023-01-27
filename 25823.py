import sys
import math
from itertools import combinations
n=int(sys.stdin.readline())
score=[20 for i in range(n+1)]
sum=[20 for i in range(n+1)]
if n==3:
    print(20)
    exit(0)
for i in range(4,n+1):
    score[i]=(score[i-1]*2+2*math.comb(2*(i-1),i-2))%(10**9+7)
    sum[i]=(sum[i-1]+score[i])%(10**9+7)

print(sum[-1])