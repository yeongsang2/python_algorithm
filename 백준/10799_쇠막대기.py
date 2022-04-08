str = input()
stack = []
cnt= 0 

for i in range(len(str)):
    if (str[i] == ')'):
        if(str[i-1] == '('):
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt +=1
    else:
        stack.append(str[i])
    
print(cnt)
        