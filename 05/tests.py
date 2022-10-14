import unittest
import sys
from random import randint
import random
import string
import os
from main import TicTacGame
from exceptions import TicTacError, IncorrectInput, \
    IncorrectValue, CellOccupied


class TestTicTacGame(unittest.TestCase):
    def test_change_step(self):
        game = TicTacGame()

        self.assertEqual(game.step, "X")

        game.change_step()

        self.assertEqual(game.step, "O")

    def test_update_board_1(self):
        game = TicTacGame()
        game.update_board("1 1")

        self.assertListEqual(
            game.board,
            [[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]],
        )

        self.assertEqual(game.step, "X")

        game.change_step()

        game.update_board("0 0")

        self.assertListEqual(
            game.board,
            [["O", " ", " "], [" ", "X", " "], [" ", " ", " "]],
        )
        self.assertEqual(game.step, "O")

    def test_validate(self):
        for _ in range(100):
            game = TicTacGame()
            row = randint(3, 9)
            col = randint(3, 9)
            move = " "*randint(0, 100) + str(row) + \
                " "*randint(0, 100) + str(col) + " "*randint(0, 100)

            self.assertRaises(IncorrectValue, game._validate, move)

    # сложные тесты с возможными пробелами
    def test_validate_input_1(self):
        for _ in range(100):
            game = TicTacGame()
            row = randint(-10, 10)
            col = randint(-10, 10)
            move = " "*randint(0, 100) + str(row) + \
                " "*randint(0, 100) + str(col) + " "*randint(0, 100)

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                self.assertRaises(TicTacError, game._validate, move)
                self.assertFalse(game.validate_input(move))
            else:
                self.assertTrue(game.validate_input(move))

    # сложные тесты с возможными пробелами
    def test_validate_input_2(self):
        for _ in range(100):
            game = TicTacGame()
            row = randint(0, 2)
            col = randint(0, 2)
            move = " "*randint(0, 100) + str(row) + \
                " "*randint(0, 100) + str(col) + " "*randint(0, 100)

            self.assertTrue(game.validate_input(move))

            game.update_board(move)

            self.assertRaises(CellOccupied, game._validate, move)
            self.assertFalse(game.validate_input(move))

    def test_validate_input_3(self):
        game = TicTacGame()
        letters = string.ascii_letters + ' '

        for _ in range(100):
            size = randint(0, 100)
            move = ''.join(random.choice(letters) for i in range(size))

            self.assertRaises(IncorrectInput, game._validate, move)
            self.assertFalse(game.validate_input(move))

    # сложные тесты с возможными пробелами
    def test_validate_input_4(self):
        for _ in range(100):
            game = TicTacGame()
            row = randint(0, 2)
            col = randint(0, 2)
            move = " "*randint(0, 100) + str(row) + \
                " "*randint(0, 100) + str(col) + " "*randint(0, 100)

            self.assertTrue(game.validate_input(move))

            game.update_board(move)

            right_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            right_board[row][col] = "X"

            self.assertListEqual(
                game.board,
                right_board,
            )

        for _ in range(100):
            game = TicTacGame()
            game.change_step()

            row = randint(0, 2)
            col = randint(0, 2)
            move = " "*randint(0, 100) + str(row) + \
                " "*randint(0, 100) + str(col) + " "*randint(0, 100)
            game.update_board(move)

            right_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            right_board[row][col] = "O"

            self.assertListEqual(
                game.board,
                right_board,
            )

    # простые тесты на победу
    def test_check_winner_1(self):
        game = TicTacGame()

        self.assertFalse(game.check_winner())

        self.assertEqual(game.step, "X")

        game.update_board("0 0")
        game.update_board("0 1")
        game.update_board("0 2")

        self.assertListEqual(
            game.board,
            [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]],
        )

        self.assertEqual(game.step, "X")

        self.assertEqual(game.check_winner(), "X")

        self.assertFalse(game.check_draw())

        game = TicTacGame()
        game.change_step()

        self.assertFalse(game.check_winner())

        self.assertEqual(game.step, "O")

        game.update_board("0 0")
        game.update_board("0 1")
        game.update_board("0 2")

        self.assertListEqual(
            game.board,
            [["O", "O", "O"], [" ", " ", " "], [" ", " ", " "]],
        )

        self.assertEqual(game.step, "O")

        self.assertEqual(game.check_winner(), "O")

        self.assertFalse(game.check_draw())

    # тест победы при прямой линии
    def test_check_winner_2(self):
        for col in range(3):
            game = TicTacGame()
            for row in range(3):
                game.update_board(f"{row} {col}")
            self.assertEqual(game.check_winner(), "X")
            self.assertFalse(game.check_draw())

        for row in range(3):
            game = TicTacGame()
            for col in range(3):
                game.update_board(f"{row} {col}")
            self.assertEqual(game.check_winner(), "X")
            self.assertFalse(game.check_draw())

        for col in range(3):
            game = TicTacGame()
            game.change_step()
            self.assertEqual(game.step, "O")
            for row in range(3):
                game.update_board(f"{row} {col}")
            self.assertEqual(game.check_winner(), "O")
            self.assertFalse(game.check_draw())

        for row in range(3):
            game = TicTacGame()
            game.change_step()
            self.assertEqual(game.step, "O")
            for col in range(3):
                game.update_board(f"{row} {col}")
            self.assertEqual(game.check_winner(), "O")
            self.assertFalse(game.check_draw())

    # тест победы при диагонали
    def test_check_winner_3(self):
        game = TicTacGame()
        game.update_board("0 0")
        game.update_board("1 1")
        game.update_board("2 2")

        self.assertEqual(game.check_winner(), "X")
        self.assertFalse(game.check_draw())

        game = TicTacGame()
        game.update_board("0 2")
        game.update_board("1 1")
        game.update_board("2 0")
        self.assertEqual(game.check_winner(), "X")
        self.assertFalse(game.check_draw())

        game = TicTacGame()
        game.change_step()
        game.update_board("0 0")
        game.update_board("1 1")
        game.update_board("2 2")

        self.assertEqual(game.check_winner(), "O")
        self.assertFalse(game.check_draw())

        game = TicTacGame()
        game.change_step()
        game.update_board("0 2")
        game.update_board("1 1")
        game.update_board("2 0")
        self.assertEqual(game.check_winner(), "O")
        self.assertFalse(game.check_draw())

    def test_check_draw(self):
        game = TicTacGame()
        for row in range(3):
            for col in range(3):
                game.update_board(f"{row} {col}")
                game.change_step()

        self.assertTrue(game.check_draw())
        self.assertFalse(game.check_winner())

    def test_integration_win(self):
        stdin_fileno = sys.stdin
        sys.stdin = open("files/input_winX.txt", "r")
        stdout_fileno = sys.stdout
        sys.stdout = open("output.txt", "w")

        game = TicTacGame()

        game.start_game()

        # иначе в файл запишутся все выводу других тестов
        sys.stdin.close()
        sys.stdin = stdin_fileno
        sys.stdout.close()
        sys.stdout = stdout_fileno

        with open("files/right_output_winX.txt", "r") as rigth_output:
            with open("output.txt", "r") as output:
                self.assertEqual(rigth_output.read(), output.read())

    def test_integration_draw(self):
        stdin_fileno = sys.stdin
        sys.stdin = open("files/input_draw.txt", "r")
        stdout_fileno = sys.stdout
        sys.stdout = open("output.txt", "w")

        game = TicTacGame()

        game.start_game()

        # иначе в файл запишутся все выводу других тестов
        sys.stdin.close()
        sys.stdin = stdin_fileno
        sys.stdout.close()
        sys.stdout = stdout_fileno

        with open("files/right_output_draw.txt", "r") as rigth_output:
            with open("output.txt", "r") as output:
                self.assertEqual(rigth_output.read(), output.read())

    @classmethod
    def tearDownClass(cls):
        os.remove("output.txt")
