import sys

example = [
    [1523, 7257, 27118, 1113001, 986, 977],
    [825, 57114, 189084, 97490, 4638, 2567],
    [8793, 246, 1461, 8628, 11464, 19867],
    [790071, 780086, 522, 7528, 97653, 2456],
    [4628, 8970, 2451, 16489, 1451, 791145]
]
###print(list(max(sum(map(int,list(str(example[k][i]))))for i in range(len(example[k])))for k in range(len(example))))
print(list(max(sum(map(int,list(str(example[k][i]))))for i in range(len(example[k])))for k in range(len(example))))
print(max(example))
print(list(max(example[k],key=lambda x:sum([int(i) for i in str(x)])) for k in range(len(example))))

print(list(max(k,key=lambda x:sum([int(i) for i in str(x)])) for k in example))