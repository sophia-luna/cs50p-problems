class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError("Capacity not accepted")
        self._capacity=capacity
        self._size=0

    def __str__(self):
        s=""
        for i in range(self.size):
            s+="🍪"
        return s

    def deposit(self, n):
        if self.size+n>self.capacity:
            raise ValueError("Too many cookies")
        self._size+=n

    def withdraw(self, n):
        if self.size-n<0:
            raise ValueError("Not enough cookies to withdraw")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size