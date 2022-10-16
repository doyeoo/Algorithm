import sys
import heapq

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    tmp = int(sys.stdin.readline())

    if tmp==0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, tmp)