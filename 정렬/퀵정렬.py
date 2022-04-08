import random

def quick_sort(arr, start, end):
    
    if start >= end: 
        return
    
    pivot  = start
    left = start +1
    right = end
    while(left <= right): #교차 전까지

        while(left <= end and arr[left] <= arr[pivot]):
            left +=1
        while(right > start and arr[right] >= arr[pivot]):
            right -=1
        if (left > right): #엇갈림
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left] 
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr,start, right-1)
    quick_sort(arr,right+1, end)

list = [0]*10
for i in range(10):
    list[i] = random.randint(0,100)

quick_sort(list, 0, len(list) -1)

for i in range(10):
    print(list[i], end=' ')
    