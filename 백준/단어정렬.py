
N = int(input())


word_list = []
for _ in range(N):
    word = input()
    word_list.append((word, len(word)))

word_list = list(set(word_list))

word_list.sort(key= lambda word : ( word[1], word[0]))

for i,v in  word_list:
    print(i)
