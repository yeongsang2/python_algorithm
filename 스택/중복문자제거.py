a = ["12","123","1235","567","88"]
a.sort()
print(a)
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
    return answer