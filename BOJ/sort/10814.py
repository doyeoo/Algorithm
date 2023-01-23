import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().strip())
# 한 줄 통으로 입력받고
# 정렬할때 숫자 단어 split해서 정렬

arr.sort(key=lambda x: int(x.split()[0]))

print("\n".join(arr))