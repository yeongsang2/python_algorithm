class MyCircularQueue:
    def __init__(self,k:int) -> None:
        self.q = [None]*k
        self.maxlen = k
        self.p1 = 0 # front
        self.p2 = 0 # rear
    def enQueue(self, value:int): # rear 포인터 이동 
        if(self.q[self.p2] is None):
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
        else:
            return False

    # dequeue front 포인터 이동
    def dequeue(self):
        if(self.q[self.p1] is None):
            return False
        else:
            val = self.q[self.p1] 
            self.q[self.p1] = None
            self.p1 = (self.p2 + 1) % self.maxlen
            return val 
    def Front(self) -> int:

        if(self.q[self.p1] is None):
            return -1
        else:
            return self.q[self.p1]    
    
    def Rear(self) -> int:
        
        if(self.q[self.p2-1] is None):
            return -1
        else:
            return self.q[self.p2-1]

    def isEmpty(self) -> bool:

        if(self.p1 == self.p2 and self.q[self.p1] is None):
            return True  
        else:
            return False      

    def isFull(self) -> bool:
        
        if(self.q[self.p2 -1] is not None and self.p1 == self.p2):
            return True

        
queue = MyCircularQueue(5)
queue.enQueue(10)
queue.enQueue(11)
queue.enQueue(12)
queue.enQueue(13)
queue.enQueue(14)


print(queue.dequeue())
print(queue.Front())
print(queue.Rear())
print(queue.isEmpty())
print(queue.isFull())
