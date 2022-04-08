num = input()
a = list(map(int, input().split()))

# max_num = max(a)
# min_num = min(a)
max_num = 0
min_num = 100
for i in a:
    if(i > max_num):
        max_num = i
for i in a:
    if(i < min_num):
        min_num = i
print(min_num,max_num)
