def solution(numbers, target):
    
    answer = 0 
    
    def dfs(csum,start):
        nonlocal answer
        if (start == 5):
            if(csum== 0):
                answer +=1
            else:
                return
        for i in range(start, len(numbers)): #range(5)
            dfs(csum+numbers[i],i+1)
            dfs(csum-numbers[i],i+1)
        
    dfs(target, 0)

    return answer
print(solution([1, 1, 1, 1, 1],3))