import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_simple(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")

        value = cache.get("k1")

        self.assertEqual(value, "val1")

    def test_size_one(self):
        cache = LRUCache(1)

        cache.set("k1", "val1")

        value = cache.get("k1")

        self.assertEqual(value, "val1")
        self.assertIsNone(cache.get("k2"))

        cache.set("k2", "val2")
        self.assertIsNone(cache.get("k1"))
        self.assertEqual(cache.get("k2"), "val2")

    def test_change_exist_key(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        # exist key
        cache.set("k3", "val1_new")

        self.assertEqual(cache.get("k3"), "val1_new")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertIsNone(cache.get("k1"))

        cache.set("k3", "val1_new2")
        cache.set("k4", "val4")

        self.assertEqual(cache.get("k3"), "val1_new2")
        self.assertEqual(cache.get("k4"), "val4")
        self.assertIsNone(cache.get("k1"))
        self.assertIsNone(cache.get("k2"))

    def test_get_none(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        value = cache.get("k3")

        self.assertIsNone(value)

    def test_limit_1(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertIsNone(cache.get("k1"))

    def test_from_hw(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIsNone(cache.get("k3"))  # None
        self.assertEqual(cache.get("k2"), "val2")  # "val2"
        self.assertEqual(cache.get("k1"), "val1")  # "val1"

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")  # "val3"
        self.assertIsNone(cache.get("k2"))  # None
        self.assertEqual(cache.get("k1"), "val1")  # "val1"

    def test_double_set(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "val3")

        self.assertIsNone(cache.get("k3"))
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val3")

    def test_long(self):
        cache = LRUCache(5)

        for i in range(100):
            cache.set(f"k{i}", f"val{i}")

            for j in range(i - 4, i+1):
                if j >= 0:
                    self.assertEqual(cache.get(f"k{j}"), f"val{j}")

            for j in range(i - 9, i - 4):
                if j >= 0:
                    self.assertIsNone(cache.get(f"k{j}"))
