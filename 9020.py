
import sys
import math
read=sys.stdin.readline
n=int(read())
result=[]
a=[False,False]+[True]*9999

for i in range(2,101):
    if a[i]:
        for i in range(2*i,10001,i):
            a[i]=False
prime=[i for i in range(2,10001) if a[i]==True]
def binary(num):
    count=math.ceil(num/2)
    first_indx=0
    last_indx=len(prime)-1
    while True:
        
        if count<prime[(first_indx+last_indx)//2]:
            last_indx=(first_indx+last_indx)//2
        elif count>prime[(first_indx+last_indx)//2]:
            first_indx=(first_indx+last_indx)//2
        elif count==prime[(first_indx+last_indx)//2]:
            return (first_indx+last_indx)//2
            break
        if first_indx+1==last_indx:
            return last_indx
            break

###print(prime)
result=[]
for i in range(n):
    x=int(read())
    ###print(binary(x))
    for j in prime[0:binary(x)+1][::-1]:
        ###print(j)
        if x-j in prime:
            ###print(x-j,j)
            if x-j>=j:
                result.append([j,x-j])
            else:
                result.append([x-j,j])
            break
for i in range(n):
    print(*result[i])




