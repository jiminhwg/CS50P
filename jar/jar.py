class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity #https://realpython.com/python-getter-setter/
        self._size = 0
        if self.capacity < 0: # If capacity is not a non-negative int, then raise a ValueError.
            raise ValueError

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        for _ in range(n):
            self._size += 1
        if self.size > self.capacity: #if # of cookies exceed max of 12 cookies
            raise ValueError

    def withdraw(self, n):
        if n > self.size: #if user withdraws more cookies than they have
            raise ValueError
        for _ in range(n):
            self._size -= 1

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(10)
print(jar)
jar.withdraw(2)
print(jar)