num = int(input())

ans = 0

for i in range(1, num+1):
    a = list(map(int, str(i)))
    ans = i + sum(a)
    if(ans ==num):
        print(i)
        break
    if(i==num):
        break
