import sys
n = int(input())
time = [ list(map(int, sys.stdin.readline().split())) for _ in range(11)]
time.sort(key=lambda x:(x[1], x[0]))
cnt = 0 
now = time[0][1]
for t in time:
    if(t[0] >= now):
        cnt +=1
        now = t[1]

print(int(cnt))

