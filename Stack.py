class Stack():

    def __init__(self):
        """
        Constructor method for class stack
        """
        self.stackList = []

    def push(self, item):
        """
        Pushes new item to the top of the stack. Requires item and returns nothing
        Runs in constant time
        """
        self.stackList.append(item)
    
    def pop(self):
        """
        Pops the item from the top of the stack. Requires nothing and returns item
        Runs in constant time
        """
        item = self.stackList[-1]
        self.stackList.remove(self.stackList[-1])
        return item

    def peek(self):
        """
        Returns the top item from the stack but does not remove it. Requires nothing and 
        returns item. 
        Runs in constant time
        """
        return self.stackList[-1]

    def isEmpty(self):
        """
        Checks to see if the stack is empty. If stack is empty, an error is raised. 
        requires nothing and returns boolean value
        """
        if len(self.stackList) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Returns number of items on the stack. Requires no parameters and returns int
        """
        return len(self.stackList)
