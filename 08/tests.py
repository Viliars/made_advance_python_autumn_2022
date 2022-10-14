import unittest
from typing import List
import string
from random import choice, randint
from collections import Counter
from anagrams import find_anagrams, EmptyPattern


# O(n)*O(m), n - длина text, m - длина pattern
def simple_find_anagrams(text: str, pattern: str) -> List[int]:
    result = []
    pattern_counter = Counter(pattern)

    for i in range(len(text)):
        text_counter = Counter(text[i:i + len(pattern)])

        if text_counter == pattern_counter:
            result.append(i)

    return result


class TestAnagrams(unittest.TestCase):
    def test_1(self):
        text = "abcaba"
        pattern = "ab"

        result: List[int] = find_anagrams(text, pattern)

        self.assertEqual(result, [0, 3, 4])

    def test_2(self):
        text = "aaaaaaa"
        pattern = "aaa"

        result: List[int] = find_anagrams(text, pattern)

        self.assertEqual(result, [0, 1, 2, 3, 4])

    def test_3(self):
        text = "lloehllo"
        pattern = "hello"

        result: List[int] = find_anagrams(text, pattern)

        self.assertEqual(result, [0, 1, 2, 3])

    def test_exception(self):
        text = "exception"
        pattern = ""

        self.assertRaises(EmptyPattern, find_anagrams, text, pattern)

    def test_lens(self):
        text = "abc"
        pattern = "abcabc"

        result: List[int] = find_anagrams(text, pattern)

        self.assertEqual(result, [])

    def test_generation(self):
        letters = string.ascii_letters

        for _ in range(1000):
            size_pattern = randint(1, 10)
            size_text = randint(size_pattern, size_pattern + 100)

            pattern = ''.join(choice(letters) for _ in range(size_pattern))
            text = ''.join(choice(letters) for _ in range(size_text))

            self.assertEqual(
                simple_find_anagrams(text, pattern),
                find_anagrams(text, pattern)
            )
