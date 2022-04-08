
import collections
T = int(input())

for _ in range(T):

    fuc = list(input())
    num = int(input())
    str = input()
    arr = collections.deque()
    for s in str:
        if s == '[' or s == ',' or s == ']':
            continue
        arr.append(int(s))
    if(num < len(arr) or not arr):
        print("error")
        continue
    for f in fuc:
        if( f == 'R'):
            if(arr):
                arr.reverse()
            else:
                print("error")
                break
        if( f == 'D'):
            if(arr):
                arr.popleft()
            else:
                print("error")
                break
    print(arr)
