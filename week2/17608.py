import sys

n = int(input())
arr = []
result = 1

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

min = arr[n-1]

for i in range(n-2, -1, -1):
    if arr[i] > min:
        min = arr[i]
        result+=1

print(result)