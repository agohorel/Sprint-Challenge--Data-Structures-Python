class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.writeptr = 0

    def increment(self):
        # incr ptr and mod by capacity to loop back around 
        self.writeptr = (self.writeptr+1) % self.capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage.pop(self.writeptr)
            self.storage.insert(self.writeptr, item)
            self.increment() # advance ptr when buffer is full

    def get(self):
        return [i for i in self.storage if i is not None]
