import sys

n=list(map(str,sys.stdin.readline().rstrip()))[::-1]
print(n)
n_1=list(map(int,n[::3]))
n_2=list(map(lambda x: 2*int(x),n[1::3]))
n_3=list(map(lambda x: 4*int(x),n[2::3]))
if len(n)%3==2:
    n_3.append(0)
if len(n)%3==1:
    n_3.append(0)
    n_2.append(0)
print(n_1,n_2,n_3)
print(''.join(map(str,[x+y+z for x,y,z in zip(n_1,n_2,n_3)][::-1])))
