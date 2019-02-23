class Deque():

    def __init__(self):
        """
        Constructor method for class Deque.
        """
        self.deque = []
       
    def addFront(self,item):
        """
        Adds a new item to the front of the deque. Requires item and returns nothing.
        """
        self.deque.insert(0,item)

    def addRear(self,item):
        """
        Adds a new item to the rear of the deque. Requires item and returns nothing.
        """
        self.deque.append(item)

    def removeFront(self):
        """
        Removes the front item from deque. Requires no parameters and returns
        item. Deque is modified.
        """
        item = self.deque[0]
        self.deque.remove(self.deque[0])
        return item

    def removeRear(self):
        """
        Removes the item from the rear of the deque. Requires no parameters and returns the item. Dque is modified.
        """
        item = self.deque[-1]
        self.deque.remove(self.deque[-1])
        return item

    def isEmpty(self):
        """
        Tests to see if the deque is empty. Requires no parameters and returns boolean value. 
        """
        if len(self.deque) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Returns the count of items in deque. Requires no parameters and returns int.
        """
        return len(self.deque)
