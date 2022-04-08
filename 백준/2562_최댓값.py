number_list = []
for _ in range(9):
    number_list.append(int(input()))

max_number = 0
for i ,v in enumerate(number_list):
    if v > max_number:
        max_number = v
        num = i

print(max_number)
print(num+1)
    
