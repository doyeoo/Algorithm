import sys

n, m = map(int, sys.stdin.readline().split()) 
set1 = set(map(int, sys.stdin.readline().split()))
set2 = set(map(int, sys.stdin.readline().split()))

result = 0

for s in set1:
    if s not in set2:
        result+=1

for s in set2:
    if s not in set1:
        result+=1

print(result)