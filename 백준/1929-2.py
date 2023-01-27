import math
x,y=input().split(' ')
x=int(x)
y=int(y)
if x==3:
    print(3)
elif 1<=x<3:
    print(2)
    print(3)
for i in range(x,y+1):
    l=int(math.sqrt(i))
    for j in range(2,l+1):
        if i%j==0:
            break
        elif j==l:
            print(i)

