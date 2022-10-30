import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split())) #이거 리스트로 안묶으면 런타임 에러남
result = 0
tmp = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = array[i]+array[j]+array[k]
            if tmp <= m:
                result = max(result, tmp)

print(result)
