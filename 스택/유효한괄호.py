

def invalid(s:str) ->bool:
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '[' 
    } #key 값 value값

    for char in s:
        if not char in table:
            stack.append(char)
        elif not stack and table[char] != stack.pop():
            return False
    

    return True

print(invalid("()[]{}"))