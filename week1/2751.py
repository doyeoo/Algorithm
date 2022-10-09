# -*- coding: utf-8 -*-

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

#quick sort
def sort(array,start,end):
    if start>= end:       
        return
    pivot = start           
    left = start + 1
    right = end
    
    while left<=right: 
        while left<=end and array[left]<=array[pivot]:
            left +=1
        while right>start and array[right]>= array[pivot]:
            right-=1
        if left>right:
            array[right],array[pivot]= array[pivot],array[right]
        else:           
            array[left],array[right]=array[right],array[left]
    sort(array, start,right-1)
    sort(array, right+1, end)

sort(arr, 0, n-1)

for i in range(n):
    print(arr[i])
