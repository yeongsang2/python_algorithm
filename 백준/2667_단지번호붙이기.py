import sys
import collections


N = int(input())
house = []
for _ in range(N):
    hou = input()
    arr = []
    for h in hou:
        arr.append(int(h))
    house.append(arr)
ans = 0
ans_house = []
def dfs(row,col,path):
    
    if (row < 0 or row >= len(house) or col < 0 or col >= len(house) or house[row][col] == 0):
        return
    house[row][col] = 0
    path.append(1)
    dfs(row+1,col, path) 
    dfs(row-1,col, path)
    dfs(row,col+1, path)
    dfs(row,col-1, path)
    return path
    
                
for i in range(len(house)):
    for j in range(len(house)):
        if (house[i][j] == 1):
            path = dfs(i,j,[])
            ans +=1
            ans_house.append(len(path))
ans_house.sort()
print(ans)
for i in ans_house:
    print(i)
        

