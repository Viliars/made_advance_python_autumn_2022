import json
import functools
import time
import numpy as np
import math
from collections import Counter

# ----- task №1 -----
def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None) -> None:
    if required_fields is None or keywords is None:
        return
    if len(required_fields) == 0 or len(keywords) == 0:
        return

    json_doc = json.loads(json_str)

    keywords = set(keywords)
    required_fields = set(required_fields)

    for_callback = []
    for key in json_doc.keys():
        if key in required_fields:
            value = json_doc[key]

            words = value.split(' ')
            for word in words:
                if word in keywords:
                    for_callback.append(word)
    
    for word in for_callback:
        keyword_callback(word)

# ----- task №2 -----

class MaxList(list):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def append(self, element):
        super().append(element)
        if super().__len__() > self.max_size:
            super().__delitem__(0)

    def get_mean(self):
        return np.mean(super().copy())


def mean(k):
    def mean_decorator(func):
        func.__logs = MaxList(k)

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            runtime = time.perf_counter() - start

            func.__logs.append(runtime)

            print(f"Mean time of {func.__name__} is {func.__logs.get_mean():.4f} secs")
            return result
        return _wrapper
    return mean_decorator

k = 3

@mean(k)
def foo(sec):
    time.sleep(sec)

stats = Counter()

def for_test(word: str) -> None:
    global stats
    stats[word] += 1

if __name__ == "__main__":
    # task №1
    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', ["key1"], ["word2"], for_test)
    assert stats['word2'] == 1
    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', ["key1"], ["Word1", "word2"], for_test)
    assert stats['Word1'] == 1
    assert stats['word2'] == 2

    # тесты MaxList
    l = MaxList(3)
    assert l == []
    l.append(1)
    assert l == [1]
    l.append(2)
    assert l == [1, 2]
    l.append(3)
    assert l == [1, 2, 3]
    l.append(4)
    assert l == [2, 3, 4]
    l.append(5)
    assert l == [3, 4, 5]
    assert math.isclose(l.get_mean(), 4.0)

    # task №2
    sum = 0
    for i in range(1, 10):
        sum += i
        foo(i)
        print(foo.__logs.get_mean(), sum / i)
        if i <= k:
            assert abs(foo.__logs.get_mean() - sum / i) < 0.1