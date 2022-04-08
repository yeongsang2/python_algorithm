import random

def insertion_sort(list, n):
    for i in range(1,n):
        key = i
        while (key > 0 and list[key-1] > list[key]): 
            list[key-1], list[key] = list[key], list[key-1]  #역순
            key -= 1

list = [0]*10
for i in range(10):
    list[i] = random.randint(0,100)


insertion_sort(list, 10)
for i in range(10):
    print(list[i], end=' ')