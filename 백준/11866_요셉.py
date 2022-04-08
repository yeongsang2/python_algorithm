
n, k = map(int, input().split())

ysp = []
deque = [i for i in range(1,n+1)]
start = 0
while(deque):
    start = (start + k -1) %len(deque)
    ysp.append(str(deque.pop(start)))


print("<%s>" %(", ".join(ysp)))



