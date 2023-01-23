import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

result1 = result2 = 0
min_value = 32

for i in range(m-7):
    for j in range(n-7):
        flag = board[j][i]
        for x in range(j, j+8):
            for y in range(i, i+8):
                if (x+y)%2==0:
                    if board[x][y]!=flag:
                        result1+=1
                    else:
                        result2+=1
                else:  
                    if board[x][y]==flag:
                        result1+=1
                    else:
                        result2+=1
        result = min(result1, result2)
        if result<min_value:
            min_value=result
            
        result=result1=result2=0

print(min_value)
