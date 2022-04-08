N = int(input())

pos = []
for _ in range(N):
    x, y  = map(int, input().split())
    pos.append((x,y))

pos.sort(key = lambda x : (x[0], x[1]))

for i, v in pos:
    print(str(i) + " " + str(v))
    