n, sum = map(int, input().split())

price_list = []
cnt = 0
for i in range(n):
    price_list.append(int(input()))

price_list.reverse()
for p in price_list:
    if(sum ==0):
        break
    while(p <= sum and sum >0):
        sum -= p
        cnt +=1
        if(sum <= 0):
            break
        
            
print(cnt)