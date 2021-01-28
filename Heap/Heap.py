import heapq

"""
    All about Heap
"""
class BinartHeap:
    def __init__(self):
        self.items=[None]
    def __len__(self):
        return len(self.items)-1

    def _percolate_up(self):
        i=len(self)
        parent=i//2
        while parent>0:
            if self.items[i]<self.items[parent]:
                ## 와 이렇게 교체할수도 있구나
                self.items[parent],self.items[i]= \
                    self.items[i],self.items[parent]
                i=parent
                parent=i//2

    def insert(self,k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self,idx):
        left=idx*2
        right=idx*2+1
        smallest=idx

        if left<=len(self) and self.items[left]<self.items[smallest]:
            smallest=left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        if smallest!=idx:
            self.items[idx],self.items[smallest]=self.items[smallest],self.items[idx]
            self._percolate_down(smallest)
            
    def extract(self):
        extracted=self.items[1]
        self.items[1]=self.items[len(self)]
        self.items.pop()    # 마지막요소 제거
        self._percolate_down(1)
        return extracted
if __name__ == '__main__':
    lst=[234,1234,43151,234,123,4,234,1,24,4]
    # Minimum Heap
    heapq.heapify(lst)  #   heapify : 리스트를 힙구조로 변환시킨다. 하지만 자료구조 자체는 리스트이다.
    pr=[]
    coplst=lst[:]
    while coplst:
        pr.append(heapq.heappop(coplst))   # Minimum 힙 정렬

    # Maximum Heap
    llst=[(-n,n) for n in lst]
    heapq.heapify(llst) #  최대힙을 구현하는 방법 튜플의 두번째 요소만 참조할 수 있겠다.
    kd=[]
    while llst:
        kd.append(heapq.heappop(llst)[1])   # 기억하
    print(kd)

    # Priority Queue

    # 튜플을 넣어주되, 첫번째 값이 우선순위, 두번재 값이 데이터이다.

