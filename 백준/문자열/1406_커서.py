import sys


stk_1 = list(sys.stdin.readline())

stk_2 = []

n = int(sys.stdin.readline())


for _ in range(n):
    a = list(sys.stdin.readline().split())

    if (a[0] == "L"):
        if(stk_1):
            stk_2.append(stk_1.pop())         
    elif( a[0]== "D"):
        if(stk_2):
            stk_1.append(stk_2.pop())
    elif( a[0] =="B"):
        if(stk_1):
            stk_1.pop()
    else:
        stk_1.append(a[1])
stk_1.extend(reversed(stk_2))
print(''.join(stk_1))