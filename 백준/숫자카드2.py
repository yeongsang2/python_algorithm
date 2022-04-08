
import sys
import collections

N = int(input())
number_card = list(map(int, sys.stdin.readline().split()))
M = int(input())
answer_card = list(map(int, sys.stdin.readline().split()))

dict = collections.defaultdict(int)

for i in number_card:
    dict[i] +=1

print(dict)

for i in answer_card:
    print(dict[i], end=' ')