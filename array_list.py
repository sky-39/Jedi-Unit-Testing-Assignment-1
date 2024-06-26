class ArrayList:
    def __init__(self):
        self.data = []
    
    def add(self, x):
        self.data.append(x)
    
    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]
    
    def remove(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data.pop(index)
    
    def size(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def clear(self):
        self.data.clear()