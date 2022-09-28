class CustomList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # функция для переиспользования кода
    def __processing(self, other, function):
        len_self = len(self)
        len_other = len(other)

        bufer = CustomList()
        for index in range(min(len_self, len_other)):
            bufer.append(function(self[index], other[index]))

        if len_self > len_other:
            for index in range(len_other, len_self):
                bufer.append(function(self[index], 0))
        else:
            for index in range(len_self, len_other):
                bufer.append(function(0, other[index]))

        return bufer

    def __add__(self, other):
        return self.__processing(other, lambda l, r: l + r)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__processing(other, lambda l, r: l - r)

    def __rsub__(self, other):
        return self.__processing(other, lambda l, r: r - l)

    def __lt__(self, other) -> bool:
        return sum(self) < sum(other)

    def __le__(self, other) -> bool:
        return sum(self) <= sum(other)

    def __eq__(self, other) -> bool:
        return sum(self) == sum(other)

    def __ne__(self, other) -> bool:
        return sum(self) != sum(other)

    def __gt__(self, other) -> bool:
        return sum(self) > sum(other)

    def __ge__(self, other) -> bool:
        return sum(self) >= sum(other)

    def __str__(self):
        return f"{super().__str__()}, {sum(self)}"
