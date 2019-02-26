class Queue():

    def __init__(self):
        """
        Constructor method for class Queue.
        """
        self.queue = []

    def enqueue(self, item):
        """
        This adds a new item to the rear of the queue. Requires item and returns nothing.
        
        Runs in constant time.
        """
        self.queue.append(item)
    
    def dequeue(self):
        """
        Removes the item from the front of the queue. Requires nothing and returns item. 
        
        Runs in linear time.
        """
        item = self.queue[0]
        self.queue.remove(self.queue[0])
        return item

    def isEmpty(self):
        """
        Tests to see if the queue is empty. Requires nothing and returns boolean value. 
        
        Runs in constant time.
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Returns the number of items in the queue. Requires nothing and returns int.
        
        Runs in constant time.
        """
        return len(self.queue)
