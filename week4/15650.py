import sys

n, m = map(int, sys.stdin.readline().split())

result = []

def ans(x):
    if len(result)==m:
        print(" ".join(map(str, result)))
        return

    for i in range(x, n+1):
        if i not in result:
            result.append(i)
            ans(i+1)
            result.pop()

ans(1)