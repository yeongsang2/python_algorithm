import sys
import heapq 

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, -x) # 최소힙이므로 역순으로 저장
    else:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    