import sys
import logging
import logging.config
from collections import deque
from config import log_config
logging.config.dictConfig(log_config)


class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.map = {}
        self.deque = deque()

        if '-s' in sys.argv:
            self.logger = logging.getLogger("to_both")
        else:
            self.logger = logging.getLogger("to_file")

        self.logger.info("LRUCache initialized")

    def get(self, key, default=None):
        if key in self.map:
            self.logger.info(f'Key "{key}" was requested')
            value = self.map[key]
            self.deque.remove(key)
            self.deque.append(key)
            return value

        self.logger.warning(f'A non-existent key "{key}" was requested')
        return default

    def set(self, key, value):
        self.logger.info(f"Adding {key}-{value}")
        if key in self.map:
            self.deque.remove(key)
        else:
            if len(self.deque) == self.limit:
                oldest_key = self.deque.popleft()
                del self.map[oldest_key]

        self.map[key] = value
        self.deque.append(key)
        self.logger.info(f"Key {key} was added")


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")

    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"
