class Node:
    def __init__(self, item, next) -> None:
        self.item = item
        self.next = next    

class Mystack:

    def __init__(self):
        self.last = None
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
    def push(self,item):
        self.last = Node(item, self.last)
    def is_empty(self):
        if(self.last == None):
            print("스택 공백")
    

        
stack = Mystack()
stack.is_empty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.last.next)