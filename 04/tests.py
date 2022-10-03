import unittest
from main import CustomList

class TestCustomListAdd(unittest.TestCase):
    def test_add_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6])

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_add_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6, 4, 5])

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3, 4, 5])

    def test_add_3(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6, 4, 5])

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3])

    def test_add_4(self):
        a = [1, 2, 3]
        b = CustomList([1, 2, 3])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6])

        self.assertIsInstance(a, list)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_add_5(self):
        a = [1, 2, 3, 4 ,5]
        b = CustomList([1, 2, 3])

        result = list(a + b)
        self.assertEqual(result, [2, 4, 6, 4, 5])

        self.assertIsInstance(a, list)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3])


    def test_add_type_1(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3])

        result = a + b
        self.assertIsInstance(result, CustomList)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3])

    def test_add_type_2(self):
        a = CustomList([1, 2, 3])
        b = [1, 2, 3]

        result = a + b
        self.assertIsInstance(result, CustomList)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, list)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_add_type_3(self):
        a = [1, 2, 3]
        b = CustomList([1, 2, 3])

        result = a + b
        self.assertIsInstance(result, CustomList)

        self.assertIsInstance(a, list)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

class TestCustomListSub(unittest.TestCase):
    def test_sub_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0])

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_sub_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0, -4, -5])

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3, 4, 5])

    def test_sub_3(self):
        a = CustomList([1, 2, 3, 4 ,5])
        b = CustomList([1, 2, 3])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0, 4, 5])

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3])

    def test_sub_4(self):
        a = [1, 2, 3]
        b = CustomList([1, 2, 3])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0])

        self.assertIsInstance(a, list)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_sub_5(self):
        a = [1, 2, 3, 4 ,5]
        b = CustomList([1, 2, 3])

        result = list(a - b)
        self.assertEqual(result, [0, 0, 0, 4, 5])

        self.assertIsInstance(a, list)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3])

    def test_sub_type_1(self):
        a = CustomList([1, 2, 3, 4 ,5])
        b = CustomList([1, 2, 3])

        result = a - b
        self.assertIsInstance(result, CustomList)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3])

    def test_sub_type_2(self):
        a = CustomList([1, 2, 3])
        b = [1, 2, 3]

        result = a - b
        self.assertIsInstance(result, CustomList)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, list)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_sub_type_3(self):
        a = [1, 2, 3]
        b = CustomList([1, 2, 3])

        result = a - b
        self.assertIsInstance(result, CustomList)

        self.assertIsInstance(a, list)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

class TestCustomListComparisons(unittest.TestCase):
    def test_eq_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertTrue(a == b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_eq_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        self.assertFalse(a == b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3, 4, 5])

    def test_eq_3(self):
        a = CustomList([1, 2, 3])
        b = CustomList([-3, 6, 3])

        self.assertTrue(a == b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [-3, 6, 3])

    def test_eq_4(self):
        a = CustomList([5, 6, 5])
        b = CustomList([6, 5, 6, -1])

        self.assertTrue(a == b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [5, 6, 5])
        self.assertEqual(list(b), [6, 5, 6, -1])

    def test_ne_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a != b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3, 4])

    def test_ne_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertFalse(a != b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_lt_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a < b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3, 4])

    def test_lt_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertFalse(a < b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_le_1(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a <= b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3, 4])

    def test_le_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertTrue(a <= b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_le_3(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3])

        self.assertFalse(a <= b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3])

    def test_gt_1(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a > b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3, 4])

    def test_gt_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertFalse(a > b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_ge_1(self):
        a = CustomList([1, 2, 3, 4, 5])
        b = CustomList([1, 2, 3, 4])

        self.assertTrue(a >= b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3, 4, 5])
        self.assertEqual(list(b), [1, 2, 3, 4]) 

    def test_ge_2(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3])

        self.assertTrue(a >= b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3])

    def test_ge_3(self):
        a = CustomList([1, 2, 3])
        b = CustomList([1, 2, 3, 4, 5])

        self.assertFalse(a >= b)

        self.assertIsInstance(a, CustomList)
        self.assertIsInstance(b, CustomList)

        self.assertEqual(list(a), [1, 2, 3])
        self.assertEqual(list(b), [1, 2, 3, 4, 5])

class TestCustomListString(unittest.TestCase):
    def test_str_1(self):
        a = CustomList([1, 2, 3])

        self.assertEqual(str(a), "[1, 2, 3], 6")

        self.assertIsInstance(a, CustomList)

        self.assertEqual(list(a), [1, 2, 3])

    def test_str_2(self):
        a = CustomList([])

        self.assertEqual(str(a), "[], 0")

        self.assertIsInstance(a, CustomList)

        self.assertEqual(list(a), [])