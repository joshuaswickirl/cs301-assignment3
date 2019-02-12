class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        item = self.queue[0]
        self.queue.remove(self.queue[0])
        return item

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)