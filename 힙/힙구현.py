class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) -1 
 
    def _percolate_up(self): #업힙
        i = len(self) # 객체의 마지막원소
        parent = i // 2 # 부모노드  //->몫
        while parent >= 0: #parent 가 0보다 클 때 까지
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i] , self.items[parent] #스와핑
            i = parent
            parent = i // 2
        
    def insert(self, k): 
        self.items.append(k)
        self._percolate_up()

    def percolate_down(self, idx):
        
        left = idx *2
        right = idx *2 +1 
        smallest = idx # 초기 idx -> 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left 
        
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self.percolate_down(smallest)

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.percolate_down(1)
        return extracted