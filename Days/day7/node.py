
class Node:
    def __init__(self, name, type, size=0):
        self.name = name
        self.type = type # file or directory
        self.size = size # only for files
        self.children = []
    
    def add_child(self, child):
        if (self.type != "directory"):
            raise Exception(f"the file {self.name} is not a directory.")
        
        self.children.append(child)
        
    def find_child_by_name(self, name):
        return list(filter(lambda item: item.name == name, self.children)).pop()