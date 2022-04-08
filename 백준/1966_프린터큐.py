

N = int(input())

for _ in range(N):
    
    total, c = map(int, input().split()) #문서개수, 궁금한 문서
    pri_list = list(map(int, input().split()))  #우선순위 표
    max_pri = max(pri_list)
    pos = 0
    answer = 1
    size_list = len(pri_list)
    while(1):
        if(pri_list[pos] == max_pri):
            pri_list[pos] = 0 #인쇄
            max_pri = max(pri_list)
            if (pos == c):
                break
            answer +=1
            pos = (pos + 1) %size_list
        else:
            pos = (pos + 1)% size_list
        
    print(answer)

                
                