import heapq
import sys

n = int(input())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)    
    if(len(heap) == 1):
        print(heap[0])
    elif(len(heap) == 2):
        print(min(heap[0], heap[1]))
    elif(len(heap) % 2 == 0): #짝수
        print(min(heap[len(heap)// 2], heap[(len(heap)//2)-1]))
    elif(len(heap) % 2 == 1):
        print(heap[len(heap)//2])
