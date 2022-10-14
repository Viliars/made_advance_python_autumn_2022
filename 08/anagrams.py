from typing import List
from collections import Counter


class EmptyPattern(Exception):
    pass


# O(n), n - длина text
def find_anagrams(text: str, pattern: str) -> List[int]:
    if len(pattern) > len(text):
        return []

    if len(pattern) == 0:
        raise EmptyPattern("pattern не может быть пустым")

    letters = Counter(text[:len(pattern)])

    pattern_letters = Counter(pattern)

    # [left, right)
    left, right = 0, len(pattern)

    result = []
    while True:
        if letters == pattern_letters:
            result.append(left)

        if right >= len(text):
            break

        letters[text[left]] -= 1
        letters[text[right]] += 1

        left += 1
        right += 1

    return result
