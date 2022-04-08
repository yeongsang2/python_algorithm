def hanoi(n,start, end ,tmp):
    if (n==1):
        print(start, end)
        return
    
    hanoi(n-1,start, tmp, end)
    print(start, end)
    hanoi(n-1,tmp,end,start)


n = int(input())
hanoi(n , 1 , 3, 2)