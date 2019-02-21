class Deque():

    def __init__(self):
        self.deque = []

    def addFront(self,item):
        self.deque.insert(0,item)

    def addRear(self,item):
        self.deque.append(item)

    def removeFront(self):
        item = self.deque[0]
        self.deque.remove(self.deque[0])
        return item

    def removeRear(self):
        item = self.deque[-1]
        self.deque.remove(self.deque[-1])
        return item

    def isEmpty(self):
        if len(self.deque) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.deque)