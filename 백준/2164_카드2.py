import collections
n = int(input())

card = collections.deque()
for i in range(n):
    card.append(i+1)

while(len(card)>1):
    card.popleft()
    a = card.popleft()
    card.append(a)

print(card.pop())

