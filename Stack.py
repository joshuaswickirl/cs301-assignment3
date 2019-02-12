class Stack():

    def __init__(self):
        self.stackList = []

    def push(self, item):
        self.stackList.append(item)
    
    def pop(self):
        item = self.stackList[-1]
        self.stackList.remove(self.stackList[-1])
        return item

    def peek(self):
        return self.stackList[-1]

    def isEmpty(self):
        if len(self.stackList) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stackList)