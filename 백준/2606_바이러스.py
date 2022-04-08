import collections

com_num = int(input())
linked_num = int(input())

dict = collections.defaultdict(list)

for i in range(linked_num):
    a,b = map(int, input().split())
    dict[a].append(b)

visited = []
def dfs(start):
    for i in dict[start]:
        if i not in visited:
            visited.append(i)
            dfs(i)
            

dfs(1)
print(len(visited))
