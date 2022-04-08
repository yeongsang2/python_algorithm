import sys


def binary_search(target, data,result): #
    start = 0
    end = len(data) -1 

    while(start <= end):
        mid = (start + end) // 2
        if(data[mid] == target):
            result.append(1)
            return
        elif(data[mid] < target):
            start = mid +1
        elif(data[mid] > target):
            end = mid -1
    result.append(0)
N = int(sys.stdin.readline())
num_card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_num = list(map(int, sys.stdin.readline().split()))
num_card.sort()
result = []
for i in check_num:
    binary_search(i, num_card,result)

for i in result:
    print(i ,end=' ')

