import sys

n = int(input())
arr = []

for _ in range(n):
    text = sys.stdin.readline().strip().split(' ')
    arr.append(text)

for i in range(n):
    result = ''
    for _ in range(len(arr[i])):
        result+=' '+arr[i].pop()
    print("Case #"+str(i+1)+":"+result)