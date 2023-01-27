import sys
read=sys.stdin.readline
word=read()

happy=len(word.split(':-)'))
sad=len(word.split(':-('))
print(happy,sad)
if happy==1 and sad==1:
    print('none')
elif happy==sad:
    print('unsure')
elif happy<sad:
    print('sad')
elif happy>sad:
    print('happy')
