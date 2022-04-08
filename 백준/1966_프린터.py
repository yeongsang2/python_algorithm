a = int(input())

for _ in range(a):
    num, p = map(int, input().split())
    pri = list(map(int, input().split()))
    answer = 0
    max_pri = max(pri)
    while(1):
        for i in range(len(pri)):
            if(pri[i] == max_pri): #프린트
                answer +=1
                pri[i] = 0 #프린트했으니까 0으로
                max_pri = max(pri)
                if(p==i):
                    print(answer)
                    break
    print(answer)





