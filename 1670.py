class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class FrontMiddleBackQueue:

    def __init__(self):
        self.front = None
        self.back = None
        self.mid = None
        self.len = 0

    def pushFront(self, val: int) -> None:
        front = Node(val)
        front.next = self.front

        self.front = front
        if not self.back:
            self.back = front
        if not self.mid:
            self.mid = front
        self.len +=1
        if (self.len + 1) % 2 == 1:
            self.mid += 1 
        elif self.len % 2 == 1:
            self.mid = self.mid.next


    def pushMiddle(self, val: int) -> None:
        mid = Node(val)
        if self.mid == None:
            self.head = mid
            self.mid = mid
            self.back = mid
            self.len += 1
        else:
            if self.len % 2 == 1:
                self.mid, mid.next = mid, self.mid
            else:
                self.mid.next, mid.next = mid, self.mid.next
                self.mid = self.mid.next

    def pushBack(self, val: int) -> None:
        

    def popFront(self) -> int:
        

    def popMiddle(self) -> int:
        

    def popBack(self) -> int: