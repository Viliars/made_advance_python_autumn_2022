from collections import deque


class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.map = {}
        self.deque = deque()

    def get(self, key, default=None):
        if key in self.map:
            value = self.map[key]
            self.deque.remove(key)
            self.deque.append(key)
            return value

        return default

    def set(self, key, value):
        if key in self.map:
            self.deque.remove(key)
        else:
            if len(self.deque) == self.limit:
                oldest_key = self.deque.popleft()
                del self.map[oldest_key]

        self.map[key] = value
        self.deque.append(key)
