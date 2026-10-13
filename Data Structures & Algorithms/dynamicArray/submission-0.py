class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        #self.array = [] * capacity #questionable
        self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        #cur = self.array.index(n)
        #self.array = self.array[:cur] + self.array[cur:] + [n]
        #self.array = self.array[:n] + self.array[n:] + [n]
        
        cur = len(self.array)
        if cur == self.capacity:
            self.resize()

        #while cur < (self.capacity - 1):
            #self.array.append(None)
            #cur += 1
        #for x in range(self.capacity - cur - 1):
        #    self.array.append(None)
            
        self.array.append(n)


    def popback(self) -> int:
        return self.array.pop(-1) #last element?

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return (len(self.array))
    
    def getCapacity(self) -> int:
        return self.capacity
