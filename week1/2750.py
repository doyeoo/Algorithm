n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
for i in range(n):
    for j in range(n):
        if arr[i] < arr[j]: 
            arr[i], arr[j] = arr[j], arr[i]

for i in range(n):
    print(arr[i])
