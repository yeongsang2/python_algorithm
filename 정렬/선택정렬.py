import random

def selection_sort(list, n):
    for i in range(0, n-1):
        least = i 
        for j in range(i+1, n):
            if (list[j] < list[least]):
                least = j
        list[i], list[least] = list[least], list[i]

max_size = 10

list = [0]*max_size
for i in range(10):
    list[i] = random.randint(1,100)

selection_sort(list, max_size)

for i in range(max_size):
    print(list[i], end=' ')
