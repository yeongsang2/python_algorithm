import heapq
import sys

num = int(input())
heap= []
for i in range(num):
    x = int(sys.stdin.readline())
    if(x):
        heapq.heappush(heap, (abs(x), x))
    else:
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    