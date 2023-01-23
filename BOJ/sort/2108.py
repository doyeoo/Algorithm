import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))   

arr.sort()

counter = Counter(arr).most_common(2)

if len(counter)>1:
    if counter[0][1]==counter[1][1]:
        mode = counter[1][0]
    else:
        mode = counter[0][0]
else:
    mode = counter[0][0]

mean = round(sum(arr)/n)
median = arr[n//2]
maxmin = max(arr)-min(arr)

print(mean)
print(median)
print(mode)
print(maxmin)