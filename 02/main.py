def near_zero(l: list) -> list:
    minimum = min(map(abs, l))
    return [l[i] for i in range(len(l)) if abs(l[i]) == minimum]

def merge(l1: list, l2: list) -> list:
    used = set()
    l1_index, l2_index = 0, 0
    result = []

    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] == l2[l2_index] and l1[l1_index] not in used:
            result.append(l1[l1_index])
            used.add(l1[l1_index])
        elif l1[l1_index] < l2[l2_index]:
            l1_index += 1
        else:
            l2_index += 1

    return result

if __name__ == "__main__":
    assert near_zero([-5, 9, 6, -8]) == [-5]
    assert near_zero([-1, 2, -5, 1, -1]) == [-1, 1, -1]
    assert near_zero([-7, 9, -13, 0]) == [0]
    assert near_zero([-7, 9, -13, -7]) == [-7, -7]
    
    lst = [1, 1, 2, 5, 7]
    tp = (1, 1, 2, 3, 4, 7)
    res = merge(lst, tp)
    assert res == [1, 2, 7]

    lst = [1, 1, 1]
    tp = (1, 2, 2, 3, 3)
    res = merge(lst, tp)
    assert res == [1]

    lst = [2, 3, 3]
    tp = (3, 3, 4)
    res = merge(lst, tp)
    assert res == [3]