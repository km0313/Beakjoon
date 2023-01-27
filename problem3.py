import sys
read=sys.stdin.readline

sample = ["전화기", "컴퓨터", "마스크", "유튜브", "비행기", "유재석"]
data = ["전퓨터", "비화기", "컴스크", "유행기", "마튜브"]
print(list((True if sample[k][0] in list(data[i][0] for i in range(len(data))) else False) for k in range(len(sample))))
print(list((True if sample[k][1:3] in list(data[i][1:3] for i in range(len(data))) else False) for k in range(len(sample))))
print([a and b for a,b in zip(list((True if sample[k][0] in list(data[i][0] for i in range(len(data))) else False) for k in range(len(sample))),list((True if sample[k][1:3] in list(data[i][1:3] for i in range(len(data))) else False) for k in range(len(sample))))])