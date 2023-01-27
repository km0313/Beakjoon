import sys
import math
n = int(sys.stdin.readline())
resu = []

for i in range(n):
    k = int(sys.stdin.readline())
    new_sco = list(map(int, sys.stdin.readline().split()))

    while True:
        print(new_sco)
        count = math.ceil(len(new_sco)/2)
        print(count)
        if len(new_sco) == 2:
            break
        rev_sco=new_sco[::-1]
        new_sco = [x+y for x,y in zip(new_sco[:count], rev_sco[:count])]
            
    if new_sco[0] > new_sco[1]:
        print(new_sco)
        resu.append('Case #'+str(i+1)+': Alice')
    else:
        print(new_sco)
        resu.append('Case #'+str(i+1)+': Bob')

print('\n'.join(resu))
