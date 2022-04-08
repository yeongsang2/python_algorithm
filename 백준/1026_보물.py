n = int(input())

A = list(map(int, input().split()))
B = list(map(int ,input().split()))

sum = 0 


min_value = min(A)
max_value = max(B)


for i in range(n):
    sum += min_value*max_value
    A.remove(min_value)
    B.remove(max_value)
    if(len(A) == 0):
        break
    min_value = min(A)
    max_value = max(B)
print(sum)