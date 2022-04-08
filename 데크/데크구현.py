from typing import List


class ListNode:
    def __init__(self,item, right, left) -> None:
        self.item= item
        self.right=right
        self.left=left

class MyCircularDequeue:
    def __init__(self,k:int) -> None:
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len  =k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에서 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    def _del(self, node:ListNode): # node right right
        n = node.right.right
        node.right = n
        n.left = node
    
    def insertFront(self, value:int):
        if self.len == self.k:
            return False
        self.len +=1
        self._add(self.head, ListNode(value))
        return True
    
    def inserLast(self, value:int):
        if self.len == self.k:
            return False
        self.len +=1
        self._add(self.tail ,ListNode(value))
        return True

    