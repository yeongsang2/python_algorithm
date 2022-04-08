n, m = map(int, input().split())

number = list(map(int, input().split()))

sum = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if(number[i]+number[j]+number[k] <= m):
                sum.append(number[i]+number[j]+number[k])

print(max(sum))