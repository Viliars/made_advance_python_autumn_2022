import unittest
from main import CustomList

class TestCustomListAdd(unittest.TestCase):
    def test_add_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6])

    def test_add_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6, 4, 5])

    def test_add_3(self):
        a = CustomList([1, 2, 3, 4 ,5])
        b = CustomList([1, 2, 3])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6, 4, 5])

    def test_add_type_1(self):
        a = CustomList([1, 2, 3, 4 ,5])
        b = CustomList([1, 2, 3])

        result = a + b
        self.assertEqual(type(result), CustomList)

    def test_add_type_2(self):
        a = CustomList([1, 2, 3])
        b = [1, 2, 3]

        result = a + b
        self.assertEqual(type(result), CustomList)

    def test_add_type_3(self):
        a = [1, 2, 3]
        b = CustomList([1, 2, 3])

        result = a + b
        self.assertEqual(type(result), CustomList)

class TestCustomListSub(unittest.TestCase):
    def test_sub_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0])

    def test_sub_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0, -4, -5])

    def test_sub_3(self):
        a = CustomList([1, 2, 3, 4 ,5])
        b = CustomList([1, 2, 3])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0, 4, 5])

    def test_sub_type_1(self):
        a = CustomList([1, 2, 3, 4 ,5])
        b = CustomList([1, 2, 3])

        result = a - b
        self.assertEqual(type(result), CustomList)

    def test_sub_type_2(self):
        a = CustomList([1, 2, 3])
        b = [1, 2, 3]

        result = a - b
        self.assertEqual(type(result), CustomList)

    def test_sub_type_3(self):
        a = [1, 2, 3]
        b = CustomList([1, 2, 3])

        result = a - b
        self.assertEqual(type(result), CustomList)

class TestCustomListEq(unittest.TestCase):
    def test_eq_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertTrue(a == b)

    def test_eq_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a != b)

class TestCustomListComparisons(unittest.TestCase):
    def test_eq_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertTrue(a == b)

    def test_eq_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        self.assertFalse(a == b)

    def test_ne_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a != b)

    def test_ne_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertFalse(a != b)

    def test_lt_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a < b)

    def test_lt_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertFalse(a < b)

    def test_le_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a <= b)

    def test_le_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertTrue(a <= b)

    def test_le_3(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3])

        self.assertFalse(a <= b)

    def test_gt_1(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a > b)

    def test_gt_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertFalse(a > b)

    def test_ge_1(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a >= b)

    def test_ge_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertTrue(a >= b)

    def test_ge_3(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        self.assertFalse(a >= b)

class TestCustomListString(unittest.TestCase):
    def test_str_1(self):
        a = CustomList([1, 2, 3])

        self.assertEqual(str(a), "[1, 2, 3], 6")

    def test_str_2(self):
        a = CustomList([])

        self.assertEqual(str(a), "[], 0")