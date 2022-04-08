import sys
import collections

n = int(sys.stdin.readline())
queue = collections.deque()
for _ in range(n):
    
    word = sys.stdin.readline().split()

    if(word[0] == "push"):
        queue.append(word[1])
    elif(word[0] == "pop"):
        if(queue):
            print(queue.popleft())
        else:
            print("-1")
    elif(word[0] == "size"):
        print(len(queue))
    elif(word[0] == "empty"):
        if(queue):
            print("0")
        else:
            print("1")
    elif(word[0] == "front"):
        if(queue):
            print(queue[0])
        else:
            print("-1")
    elif(word[0] == "back"):
        if(queue):
            print(queue[-1])
        else:
            print("-1")
        

