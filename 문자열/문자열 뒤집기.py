def reverseString(s: list[str]) ->None:
    left, right = 0, len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    print(s)

def reverseString2(s: list[str]):
    s.reverse()
    print(s)

s = ["h", "e","l", "l",'o']
print(s)
#reverseString(s)   
reverseString(s)

