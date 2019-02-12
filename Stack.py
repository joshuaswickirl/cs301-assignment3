class Stack():

    def __init__(self):
        self.stackList = []

    def push(self, item):
        self.stackList.append(item)
    
    def pop(self):
        self.stackList.remove(self.stackList[-1])

    def peek(self):
        return self.stackList[-1]

    def isEmpty(self):
        if len(self.stackList) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stackList)