
n, m = map(int, input().split())
solve = [] #중복 체크
def back(depth):
    if(depth==m):
        for i in solve:
            print(i, end=' ')
        print()
    for i in range(1,n+1):
        if i not in solve:
            solve.append(i)
            back(depth+1)
            solve.pop()
back(0)
