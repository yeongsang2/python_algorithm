
def dfs(now, depth,answer):
    
    if(num_list[now] in answer):
        return
    
    if(len(answer) == 6):
        print(answer)
        answer.pop()
        return
    
    #answer.append(num_list[now])
    for i in range(now+1, len(num_list)):
        answer.append(num_list[i])
        dfs(i,depth+1,answer)
    return
    
result = []
num_list = list(map(int, input().split()))
first = num_list.pop(0)

dfs(0,0,[])
print(result)