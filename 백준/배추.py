import sys

sys.setrecursionlimit(100000)

T = int(input())

def dfs(i, j):
    if(i < 0 or i >= N or j < 0 or j >= M or land[i][j] == 0):
        return
    land[i][j] = 0
    dfs(i-1,j)
    dfs(i+1,j)
    dfs(i,j-1)
    dfs(i,j+1)  
    return

for t in range(T):
    M, N, K = map(int, input().split()) #가로, 세로, 배추 개수
    land = []
    for _ in range(N):
        arr = [0]*M
        land.append(arr)
    
    for _  in range(K):
        a, b =map(int, sys.stdin.readline().split())
        land[b][a] = 1
    
    ans = [0]*T
    for i in range(N):
        for j in range(M):
            if(land[i][j] == 1):
                dfs(i, j)
                ans[t] +=1 
    print(ans[t])
