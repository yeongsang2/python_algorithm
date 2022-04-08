import collections


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagram = collections.defaultdict(list)
        
    for word in strs:
        sorted(word)
        anagram[''.join(sorted(word))].append(word)

    return anagram.values()


