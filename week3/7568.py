import sys

n = int(sys.stdin.readline())
w = []
result = []
rank = 1

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    w.append((x, y))

for i in range(n):
    for j in range(n):
        if w[i][0]<w[j][0] and w[i][1]<w[j][1]:
            rank+=1
    print(rank, end=' ')
    rank = 1