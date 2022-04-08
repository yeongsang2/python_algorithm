n = int(input())


check = 0
for _ in range(n):
    word = input()
    stack = []
    a= 0
    for w in word:
        if w in stack:
            if(stack[-1] != w):
                a = 1
                break
        stack.append(w)
    if (a == 0):
        check +=1

print(check)
