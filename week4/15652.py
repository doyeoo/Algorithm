import sys

n, m = map(int, sys.stdin.readline().split())

result = []

def ans(status):
    if len(result)==m:
        print(" ".join(map(str, result)))
        return

    for i in range(status, n+1):
        result.append(i)
        ans(status)
        result.pop()
        status = status+1

ans(1)
