import sys

n = int(input())
arr = []

for _ in range(n):
    text = sys.stdin.readline().strip().split(' ')
    
    if text[0]=='push':
        arr.append(text[1])
    if text[0]=='pop':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    if text[0]=='size':
        print(len(arr))
    if text[0]=='empty':
        if not arr:
            print(1)
        else:
            print(0)
    if text[0]=='top':
        if arr:
            print(arr[-1])
        else:
            print(-1)
