import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 첫번째 원소 먼저 보고 동일하면 두번째 원소로 정렬
arr.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    print(arr[i][0], arr[i][1], sep=' ')