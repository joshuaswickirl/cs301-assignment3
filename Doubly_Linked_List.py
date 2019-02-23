class List():

    def __init__(self):
        """
        Constructor method for class List. 
        """
        self.head = None
    
    def add(self,item):
        """
        Adds new item to the beginning of the list. Requires item and returns nothing.
        """
        pass

    def remove(self,item):
        """
        Removes item from the list. Requires item and modifies the list, 
        if item isnt in list it raises an error.  
        """
        pass

    def search(self,item):
        """
        Searches list for item, requires item and returns boolean value
        """
        pass

    def isEmpty(self):
        """
        Checks to see if the list is empty, requires nothing and returns boolean values
        """
        pass

    def size(self):
        """
        Returns the count of the list, requires nothing and returns int
        """
        pass
    
    def append(self,item):
        """
        Adds new item to the end of the list, requires item and returns nothing
        """
        pass

    def index(self,item):
        """
        Returns position of item in list. Requires item and returns index. 
        If item is not in list it raises an error. 
        """
        pass

    def insert(self,pos,item):
        """
        Adds an instance of item at position pos. Requires item and returns nothing. 
        """
        pass

    def pop(self):
        """
        Removes and returns the last item in the list. Requires item and returns nothing. 
        If the list is empty, an error is raised.
        """
        pass

    def pop(self,pos):
        """
        Returns and removes an instance of item at position pos. Requires position and item. 
        If list is too short, error is raised.
        """
        pass

    def print(self):
        """
        Prints the list. 
        """
        node = self.head
        while node is not None:
            print(f"Current node data: {node.get_data()}, next node: {node.get_next_node()}")
            node = node.get_next_node()

class Node():

    def __init__(self, input_data):
        """
        Constructor method for class Node.        
        Runs in constant time
        """
        self.data = input_data
        self.next_node = None
        self.previous_node = None
    
    def get_data(self):
        """
        Gets a reference to the data. Requires nothing and returns data.
        Runs in constant time
        """
        return self.data

    def set_data(self, new_data):
        """
        Sets a reference to the data. Requires new_data and returns nothing. 
        Runs in constant time
        """
        self.data = new_data

    def get_next_node(self):
        """
        Gets a reference to the next node. Requires nothing and returns new_data
        Runs in constant time
        """
        return self.next_node

    def set_next_node(self, new_next_node):
        """
        Sets a reference to the next node. Requires new_next_node and returns nothing.
        Runs in constant time
        """
        self.next_node = new_next_node

    def get_previous_node(self):
        """
        Gets a reference to the previous node. Requires nothing and returns the prevoius node
        Runs in constant time
        """
        return self.previous_node

    def set_previous_node(self, new_previous_node):
        """
        Sets a refrence to the previous node. Requires new_previous_node and returns nothing. 
        Runs in constant time
        """
        self.previous_node = new_previous_node
