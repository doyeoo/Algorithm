import sys

n, m = map(int, sys.stdin.readline().split())

result = []

def ans():
    if len(result)==m:
        print(" ".join(map(str, result)))
        return

    for i in range(1, n+1):
        result.append(i)
        ans()
        result.pop()

ans()