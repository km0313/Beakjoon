import sys
read=sys.stdin.readline
'''graph = {
    1: [2,5,9],
    2: [3],
    3: [4],
    4: [],
    5: [6,8],
    6: [7],
    7: [],
    8: [],
    9: [10],
    10: []
}'''
n=int(read())
bintree=dict()


for i in range(n):
    u,v1,v2=map(str,read().split())
    bintree[u]=[]
    bintree[u].append(v1)
    bintree[u].append(v2)


'''def preorder(i):
    lf,rt=bintree[i]
    result.append(i)
    print(result)
    if lf=='.' and rt=='.':
        return 0
    else:
        if lf!='.':
            preorder(lf)
        if rt!='.':
            preorder(rt)
'''
def preorder(i):
    lf,rt=bintree[i]
    print(i,end='')
    if lf!='.':
        preorder(lf)
    if rt!='.':
        preorder(rt)


'''def inorder(i):
    lf,rt=bintree[i]
    print(result)
    if lf!='.':
        inorder(lf)
        result.append(lf)
        print('lf')
        print(result)
    
    result.append(i)
    print('i')
    print(result)    
    if rt!='.':
        inorder(rt)
        
        print('rt!')
'''
def inorder(i):
    lf,rt=bintree[i]
    
    if lf!='.':
        inorder(lf)
    print(i,end='')
    if rt!='.':
        inorder(rt)
        
        
    

'''def postorder(i):
    lf,rt=bintree[i]
    if len(result)==n-1:
        result.append('A')
    print(result)
    if lf!='.':
        postorder(lf)
        result.append(lf)
    if rt!='.':
        postorder(rt)
        result.append(rt)
  '''  
def postorder(i):
    lf,rt=bintree[i]
    if lf!='.':
        postorder(lf)
    if rt!='.':
        postorder(rt)  
    print(i,end='')  


    

    
    
preorder('A')
print(end='\n')
inorder('A')
print(end='\n')
postorder('A')
    

    

    

