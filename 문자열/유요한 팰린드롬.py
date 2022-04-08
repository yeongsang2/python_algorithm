def isPalindrome(s:str)-> bool:
    strs = []

    

    for char in s:
        if char.isalnum(): # 문자일경우
            strs.append(char.lower())
    
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
        
    return True


ex = "A man, a plan, a canal: panama"
print(isPalindrome(ex))


