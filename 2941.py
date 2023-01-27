import sys

read=sys.stdin.readline
words=list(read().rstrip())
leg=0

while True:
    if len(words)==0:
        break
    if len(words)>=3:
        word=''.join(words[:3])
        if word=='dz=':
            leg+=1
            words=words[3:]
            print(word,leg)
            continue

    if len(words)>=2:    
        word=''.join(words[:2])
        if word=='c='or word=='c-'or word=='d-'or word=='lj'or word=='nj'or word=='s='or word=='z=':
            leg+=1
            words=words[2:]
            print(word,leg)
            continue
        
    if len(words)>=1:
        leg+=1
        print(words[0],leg)
        words=words[1:]
    
print(leg)
