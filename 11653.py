import sys
import math
n=int(sys.stdin.readline())

def fac(i):
    ###print('fac')
    if i==1:
        return None
    maxnum=math.ceil(i**(1/2))
    ###print(maxnum)
    for k in range(2,maxnum+1):
        if i%k==0:
            print(k)
            fac(i/k)
            return None
    print(int(i))
    
    
fac(n)
