import collections
N, M = map(int, input().split())

map = []
for i in range(N):
    str = input()
    arr = [ int(s) for s in str]
    map.append(arr)

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0,0,-1,1] # 상 하 좌 우
stack = collections.deque()
stack.append([0,0])

while(stack):
    x,y = stack.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if( nx >= 0 and nx < N and ny >= 0 and ny < M and map[nx][ny] == 1):
            map[nx][ny] = map[x][y] +1                
            stack.append([nx,ny])
for i in map:
    print(i)      
print(map[N-1][M-1])
