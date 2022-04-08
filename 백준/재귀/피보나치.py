def fiv(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1 
    return fiv(n-1) + fiv(n-2)   


def fiv_repeat(n):
    if(n==1): return 1
    if(n==0): return 0
    pp = 0
    p =1
    result = 0
    for i in range(2,n+1):
        result = p + pp
        pp = p
        p = result
    return result 


num = int(input())

print(fiv(num))