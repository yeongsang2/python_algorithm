import random

def merge_sort(numbers):
    
    n = len(numbers)

    if n <=1 :
        return 
    mid = n // 2
    left_groups = numbers[:mid]
    right_groups = numbers[mid:]
    
    merge_sort(left_groups)
    merge_sort(right_groups)

    left = 0
    right = 0
    now = 0
    
    while left < len(left_groups) and right < len(right_groups):
        if left_groups[left] < right_groups[right]:
            numbers[now] = left_groups[left]
            left +=1
            now +=1
        else:
            numbers[now] = right_groups[right]
            right +=1
            now +=1
    while(left < len(left_groups)): # right 가 먼저 채워짐
        numbers[now] = left_groups[left]
        now +=1
        left +=1
    while(right < len(right_groups)):
        numbers[now] = right_groups[right]
        now +=1
        right +=1
    

list = [0]*10
for i in range(10):
    list[i] = random.randint(0,100)

merge_sort(list)

for i in range(10):
    print(list[i], end=' ')
    