import sys
import collections

N, M, V= map(int, input().split())
dic = collections.defaultdict(list)
for i in range(M):
    a, b= map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
    dic[a].sort()
    dic[b].sort()

print(dic)

dfs_path = [V]
bfs_path = [V]
def dfs(dict, start):
    print(start, end=' ')
    for i in dict[start]:
        if i not in dfs_path:
            dfs_path.append(i)
            dfs(dict, i)
    
def bfs(dict, start):
    queue = [start]
    while(queue):
        cur = queue.pop(0)
        print(cur, end = ' ')
        for i in dict[cur]:
            if i not in bfs_path:
                bfs_path.append(i)
                queue.append(i)

dfs(dic, V)
print()
bfs(dic, V)