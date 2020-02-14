# 1|2|3
# 4|5|6
# 7|8|9
import random


class Board:

    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        return False

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def sign_printable(self, sign):
        if sign == 0:
            return ' '
        elif sign == 1:
            return 'X'
        else:
            return 'O'

    def print_board(self):
        print(' ' + self.sign_printable(self.state[0]) + ' | ' + self.sign_printable(
            self.state[1]) + ' | ' + self.sign_printable(self.state[2]))
        print(' ' + self.sign_printable(self.state[3]) + ' | ' + self.sign_printable(
            self.state[4]) + ' | ' + self.sign_printable(self.state[5]))
        print(' ' + self.sign_printable(self.state[6]) + ' | ' + self.sign_printable(
            self.state[7]) + ' | ' + self.sign_printable(self.state[8]))

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def check_win(self, symbol):
        s = symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True
        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True
        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True


class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def make_turn(self, cell):
        board.state[cell] = self.symbol


class ComP(Player):

    def random_com_move(self):
        i = random.randint(0, 8)
        while not board.is_valid_turn(i):
            i = random.randint(0, 8)
        return i

    def check_com_win(self):
        for i in range(0, len(board.state)):
            if board.is_valid_turn(i):
                player2.make_turn(i)
                if board.check_win(2):
                    return i
                else:
                    board.state[i] = 0
        return -1

    def check_enemy_win(self):
        for i in range(len(board.state)):
            if board.is_valid_turn(i):
                player1.make_turn(i)
                if board.check_win(1):
                    return i
                else:
                    board.state[i] = 0
        return -1


if __name__ == '__main__':
    player1 = Player(1)
    player2 = ComP(2)
    board = Board()
    active_P = player1
    while not board.is_full():
        if active_P == player2:
            cell = player2.check_com_win()
            if cell == -1:
                cell = player2.check_enemy_win()
                if cell == -1:
                    cell = player2.random_com_move()
            player2.make_turn(cell)
            board.make_turn(cell, player2)
            if board.check_win(player2.symbol):
                print('Der PC hat gewonnen')
                board.print_board()
                break
        else:
            board.print_board()
            try:
                cell = int(input('Geben Sie an in welcher Zeile Sie setzen wollen [1-9]: '))
            except ValueError:
                continue
            if cell < 0 or cell > 9:
                print('Ungültige Eingabe')
                continue
            if not board.make_turn(cell - 1, player1):
                print('Ungültige Eingabe')
                continue
        if board.check_win(player1.symbol):
            print('Glückwunsch du hast gewonnen')
            board.print_board()
            break
        elif active_P == player1:
            active_P = player2
        else:
            active_P = player1
    if board.is_full():
        print('Unentschieden')