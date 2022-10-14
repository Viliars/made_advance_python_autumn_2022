import os
import re
from exceptions import IncorrectInput, IncorrectValue, CellOccupied


BOARD_SIZE = 3


class TicTacGame:
    def __init__(self):
        self.board = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.step = "X"
        self.validate_pattern = re.compile(r"^\s*(\d)\s*(\d)\s*$")
        self.next_step = False

    def show_board(self):
        print("---------------")
        for row in self.board:
            print("", *row, sep=" | ", end=" |\n")
            print("---------------")

    def input(self):
        print(f"Сейчас ход игрока {self.step}")
        move = input("Введите строку и столбец 0..2 0..2 = ")
        return move

    def _validate(self, move):
        if not self.validate_pattern.match(move):
            raise IncorrectInput()

        row, col = map(int, self.validate_pattern.findall(move)[0])

        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
            raise IncorrectValue()

        if self.board[row][col] != " ":
            raise CellOccupied()

        return True

    def validate_input(self, move):
        self.next_step = False

        try:
            if self._validate(move):
                self.next_step = True
                return True
        except IncorrectInput:
            print("Некорректный ввод")
        except IncorrectValue:
            print("Некорректный ввод")
            print("Строка и столбец выбираются из промежутка от 0 до 2")
            print("Пример: 1 1")
        except CellOccupied:
            print("Выбранная клетка занята")
            print("Пожалуйста, выберите другую клетку")

        return False

    def update_board(self, move):
        row, col = map(int, self.validate_pattern.findall(move)[0])
        self.board[row][col] = self.step
        return True

    def change_step(self):
        if self.step == "X":
            self.step = "O"
        else:
            self.step = "X"

    def check_winner(self):
        # горизонтальные прямые
        for line in self.board:
            if line.count(self.step) == BOARD_SIZE:
                return self.step

        # вертикальные прямые
        for line in map(list, zip(*self.board)):
            if line.count(self.step) == BOARD_SIZE:
                return self.step

        # диагональная прямая
        diag_line = [self.board[i][i] for i in range(BOARD_SIZE)]
        count_on_diag = diag_line.count(self.step)
        if count_on_diag == BOARD_SIZE:
            return self.step

        # диагональная прямая
        diag_line = [self.board[i][BOARD_SIZE-i-1] for i in range(BOARD_SIZE)]
        count_on_diag = diag_line.count(self.step)
        if count_on_diag == BOARD_SIZE:
            return self.step

        return False

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def start_game(self):
        os.system("clear")

        while True:
            self.show_board()
            move = self.input()

            if self.validate_input(move):
                self.update_board(move)

                winner = self.check_winner()
                if winner:
                    self.show_board()
                    print(f"Игрок {winner} победил!")
                    return

                if self.check_draw():
                    self.show_board()
                    print("В упорной борьбе произошла ничья!")
                    return

                if self.next_step:
                    self.change_step()


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
