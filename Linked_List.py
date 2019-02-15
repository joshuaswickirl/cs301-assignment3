class List():
    
    def __init__(self):
        self.head = None
    
    def add(self,item):
        new_node = Node(item)
        new_node.set_next_node(self.head)
        self.head = new_node
        
    def remove(self,item):
        current_node = self.head
        last_node = None
        item_found = False
        while not item_found:
            if current_node.data == item:
                next_node = current_node.get_next_node()
                del current_node
                if last_node == None:
                    self.head = next_node
                else:
                    last_node.set_next_node(next_node)
                item_found = True
            else:
                # prep for next iteration
                last_node = current_node
                current_node = current_node.get_next_node()

    def search(self,item):
        node = self.head
        item_found = False
        while not item_found:
            if node.data == item:
                item_found = True
            else:
                node = node.get_next_node()
                if node == None:
                    break
        return item_found

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        num_nodes = 0
        node = self.head
        while node is not None:
            num_nodes += 1
            node = node.get_next_node()
        return num_nodes
    
    def append(self,item):
        pass

    def index(self,item):
        pass

    def insert(self,pos,item):
        pass

    def pop(self,pos=None):
        pass

    def print(self):
        node = self.head
        while node is not None:
            print(node.get_data())
            node = node.get_data()[1]

class Node():
    def __init__(self, input_data):
        self.data = input_data
        self.next_node = None
    
    def get_data(self):
        return [self.data, self.next_node]

    def set_data(self, new_data):
        self.data = new_data

    def get_next_node(self):
       return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node