def hanoi(n,start,tmp,to):
    if(n==1):
        print(start,to)
        return
    hanoi(n-1,start,to,tmp)
    print(start,to)
    hanoi(n-1,tmp,start,to)


a = int(input())
hanoi(a,1,2,3)

