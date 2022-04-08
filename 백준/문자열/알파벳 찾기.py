
alp ='abcdefghijklmnopqrstuvwxyz'
str = str(input())

for i in alp:
    if i in str:
        for a,b in enumerate(str):
            if i == b:
                print(a, end=' ')
                break
    else:
        print(-1,end=' ')
