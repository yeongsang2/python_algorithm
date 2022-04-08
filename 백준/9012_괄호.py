a = int(input())

for _ in range(a):
    stack = []
    str = input()
    for s in str:
        if(s== '('):
            stack.append(s)
        else:
            if(not stack):
                print("NO")
                break
            else:
                stack.pop()     
    if(len(stack)==0):
        print("YES")
    else:
        print("NO")
            
    

