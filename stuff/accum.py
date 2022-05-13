

class Accumlator:

    def __init__(self):
        self.count = 0

    @property
    def count(self):
        return self.count
    
    def add(self, more=1):
        self.count += more