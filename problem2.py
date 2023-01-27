import sys
read=sys.stdin.readline
example = [0,-1,-2,-3]


print(list([1 if i==k else 0 for i in range(0,max(example)+1)] for k in filter(lambda x:x>=0,example)))