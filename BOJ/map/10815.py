import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()

def search(x):
    start = 0
    end = n-1

    #이진탐색
    while start<=end:
        mid = (start+end)//2

        if arr1[mid]==x:
            return 1
        if arr1[mid]<x:
            start = mid+1
        if arr1[mid]>x:
            end = mid-1

    return 0

result = list(map(search, arr2))

for r in result:
    print(r, end=' ')