a = int(input())

person = []
rank = [1]*a
for _ in range(a):
    p  = list(map(int, input().split()))
    person.append(p)
for i in range(a):
    for j in range(a):
        if(j==i):
            continue
        if(person[i][0] < person[j][0] and person[i][1] < person[j][1]):
            rank[i] +=1

for i in range(a):
    print(rank[i], end=' ')