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
        Removes item from the list. Requires item and modifies the list, if item isnt in list it raises an error.  
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
        
        """
        pass
    
    def append(self,item):
        pass

    def index(self,item):
        pass

    def insert(self,pos,item):
        pass

    def pop(self):
        pass

    def pop(self,pos):
        pass

    def print(self):
        pass


class Node():

    def __init__(self, input_data):
        self.data = input_data
        self.next_node = None
        self.previous_node = None
    
    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

    def get_previous_node(self):
        return self.previous_node

    def set_previous_node(self, new_previous_node):
        self.previous_node = new_previous_node
