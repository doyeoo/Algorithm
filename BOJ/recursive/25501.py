import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().strip())

def recursion(s, l, r, num):
    if l >= r: return str(1)+" "+str(num)
    elif s[l] != s[r]: return str(0)+" "+str(num)
    else: return recursion(s, l+1, r-1, num+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for i in range(n):
    print(isPalindrome(arr[i]))