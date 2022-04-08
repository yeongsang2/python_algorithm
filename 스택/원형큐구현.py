class MyCircularQueue:
    def __init__(self, k:int):
        self.q = [None]*k
        self.maxlen = k
        self.p1 = 0 #front 
        self.p2 = 0  #rear

    def enQueue(self, value:int):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 +1) % self.maxlen
            return True
        else:
            return False
    # dequeue front 포인터 이동
    def dequeue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 +1 ) % self.maxlen
            return True
    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self) -> int:
        return -1 if self.q[self.p2] is None else self.q[self.p2]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.pq] is not None

queue = MyCircularQueue(5)
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)