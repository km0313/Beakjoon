import sys
import itertools
from functools import reduce
data = [
    "What is the point in saying that when you know how I will react",
    "You think you can just take it back but shit just dont work like that",
    "You are the drug that I am addicted to and I want you so bad",
    "Guess I am stuck with you and that is that"
]
sample = [
    "What is the trick",
    "I wish I knew",
    "I am so done with thinking through all the things I could have been",
    "And I know you want me too",
    "All it takes is that one look at you and I run right back to you",
    "You cross the line and it is time to say F you"
]
new_sample=dict.fromkeys(sorted(map(lambda x :x.lower(),reduce(lambda x,y:x+' '+y,sample).split())))
count=0
for i in new_sample:
    new_sample[i]=count
    count+=1
print(new_sample)
answer=list(list(map(lambda x :x.lower() ,i.split() )) for i in data)
print(new_sample)
###for words in answer:
###    for word in words:
###        new_sample[word]
print([[len(new_sample) if new_sample.get(word)==None else new_sample.get(word) for word in words] for words in answer])
###print(new_sample.find('sdsdsd'))