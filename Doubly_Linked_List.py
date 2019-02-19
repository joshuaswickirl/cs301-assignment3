class List():

    def __init__(self):
        self.head = None
    
    def add(self,item):
        pass

    def remove(self,item):
        pass

    def search(self,item):
        pass

    def isEmpty(self):
        pass

    def size(self):
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
        node = self.head
        while node is not None:
            print(f"Current node data: {node.get_data()}, next node: {node.get_next_node()}")
            node = node.get_next_node()


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