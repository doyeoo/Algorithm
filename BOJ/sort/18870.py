import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

new_list = list(set(arr))
new_list.sort()

dic = {}

for i in range(len(new_list)):
    # 딕셔너리 추가할 때에는 이렇게
    dic[new_list[i]] = i

for a in arr:
    print(dic[a], end=' ')

# arr.index(a)로 하면 매번 다 순회하면서 찾는거라 O(n)
# 모든 원소마다 n번씩 돌면 복잡도 망함

# 딕셔너리 dic[key]는 조회 삽입 모두 시간복잡도 O(1) 굿
