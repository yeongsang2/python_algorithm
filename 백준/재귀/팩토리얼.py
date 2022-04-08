def recursive(n):
    if(n == 0):
        return 0
    if(n ==1):
        return 1
    return n*recursive(n-1)

def recursive_1(n):
    if(n == 0):
        return 0
    if(n ==1):
        return 1
    return recursive(n-1)*n

def recursive_rep(n):

    result =1 
    for i in range(n,0,-1):
        print(i)
        result = result*i
    return result
def ex(n):
    if n==1 :
        return 1
    else:
        return 1 / n + ex(n-1)
    

    

N = int(input())
# print(recursive_1(N))
# print(recursive(N))
# print(recursive_rep(N))
print(ex(N))