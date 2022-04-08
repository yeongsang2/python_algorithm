import re
import collections

def mostCommonWord(paragraph:str, banned: list[str]):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    
    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]

banned = ["hit"]
paragraph = "Bob hit a ball, hte hit BALL flew far after it was hit"
print(mostCommonWord(paragraph, banned))