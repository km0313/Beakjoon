import sys

score=[0 for i in range(10001)]
n=int(sys.stdin.readline())
for i in range(n):
    score[int(sys.stdin.readline())]+=1
    
for i in range(1,10001):
    if score[i]==0:
        continue
    for k in range(score[i]):
        print(i)
'''
a=[1]
a[0]+=1
print(a[0])

print([0 for i in range(10)])
'''
