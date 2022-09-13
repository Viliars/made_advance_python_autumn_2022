import math
from time import time
from random import randint

def square_solution(a: float, b: float, c:float) -> tuple | None:
    # посчитаем дискриминант
    D = b ** 2 - 4 * a * c
 
    if D > 0:
        return (-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)
    elif D == 0:
        x = -b / (2 * a)
        return x, x
    else:
        return None

def split_v1(x: list) -> tuple[list, list]:
    # решение с одним проходом по массиву
    odd_list = []
    even_list = []
    for elem in x:
        if elem % 2 == 0:   even_list.append(elem)
        else:   odd_list.append(elem)
    return even_list, odd_list

def split_v2(x: list) -> tuple[list, list]:
    # такое решение пробегается по массиву дважды, но в теории может быть не сильно медленнее,
    # чем решение V1, потому что генераторы списков работают быстро
    return [elem for elem in x if elem % 2 == 0], [elem for elem in x if elem % 2 == 1]

def time_test(size: int, count_experiments: int = 10) -> None:
    x = [randint(0, 10000) for _ in range(size)]

    start_v1 = time()
    for _ in range(count_experiments):
        result_v1 = split_v1(x)
    end_v1 = time()

    start_v2 = time()
    for _ in range(count_experiments):
        result_v2 = split_v2(x)
    end_v2 = time()

    assert result_v1 == result_v2
    return (end_v1 - start_v1), (end_v2 - start_v2)

if __name__ == "__main__":
    # task1
    assert square_solution(-1, 7, 8) in [(-1, 8), (8, -1)]
    assert square_solution(4, 4, 1) in [(-0.5, -0.5), (-0.5,)]
    assert square_solution(2, 1, 1) is None

    # task2 
    assert split_v1([1, 2, 3, 4, 5]) == ([2, 4], [1, 3, 5])
    assert split_v2([1, 2, 3, 4, 5]) == ([2, 4], [1, 3, 5])

    assert split_v1([1, 3, 5, 7, 9]) == ([], [1, 3, 5, 7, 9])
    assert split_v2([1, 3, 5, 7, 9]) == ([], [1, 3, 5, 7, 9])

    assert split_v1([2, 4, 6, 8]) == ([2, 4, 6, 8], [])
    assert split_v2([2, 4, 6, 8]) == ([2, 4, 6, 8], [])

    # --- speed comparison ---
    for size in [100, 1000, 10000, 100000, 1000000]:
        v1, v2 = time_test(size)
        print(f"Size: {size:7d}; V1: {v1:.5f}; V2: {v2:.5f}; speed_down={v2/v1:.2f}")

    # результат - V2 версия в среднем медленнее V1 всего на 15%