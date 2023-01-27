a=int(input())

l=int(a/5)
l_3=0
for i in range(l,-1,-1):
    x_3=a-i*5
    l_3=x_3/3
    if (x_3%3)==0:
        print(int(i+l_3))
        break
    elif i==0:
        print(-1)
