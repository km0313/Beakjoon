import sys
import time
read=sys.stdin.readline
n=int(read())


def honoi(num,counting=0,srt=1,via=2,dst=3):
    global counter
    if num==1:
        print(srt,dst)
        
        return 0
    else:
        honoi(num-1,counting,srt,dst,via)
        print(srt,dst)
        
        honoi(num-1,counting,via,srt,dst)
###start_time=time.time()
print(2**n-1)
if n<=20:
    honoi(n)

        
###end_time=time.time()
###print(end_time-start_time)

    
    