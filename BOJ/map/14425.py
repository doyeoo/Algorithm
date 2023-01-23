import sys

n, m = map(int, sys.stdin.readline().split()) 
s = set()
test = []
result = 0

for _ in range(n):
    s.add(sys.stdin.readline().strip())

for _ in range(m):
    test.append(sys.stdin.readline().strip())

for t in test:
    if t in s:
        result+=1

print(result)