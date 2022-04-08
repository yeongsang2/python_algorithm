
n = int(input())
stk = []

answer = []
check = 1
cur = 1 
for i in range(n):
    num = int(input())
    while (cur <= num):
        stk.append(cur)
        answer.append('+')
        cur +=1 
    if(stk[-1] == num):
        stk.pop()
        answer.append('-')
    else:
        check =0
        break
if check:
    for i in answer:
        print(i)
else:
    print("NO")

