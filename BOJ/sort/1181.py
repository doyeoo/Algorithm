import sys

n = int(sys.stdin.readline())
arr = set()

for _ in range(n):
    arr.add(sys.stdin.readline().strip())

new_arr = list(arr)
new_arr.sort(key=lambda x: (len(x), x))
print("\n".join(new_arr))