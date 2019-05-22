#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.reflectcount = 0
        self.cyclecount = 0

    def move(self):
        return 'rock'

    def learn(self, my_move):
        pass

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):

    def move(self):
        message = input('Rock, paper, scissors? > ').lower()
        while message not in moves:
            message = input('Rock, paper, scissors? > ').lower()
        return message


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):

    def learn(self, my_move):
        self.my_move = my_move

    def move(self):
        if self.reflectcount == 0:
            return moves[0]
        elif self.reflectcount >= 1:
            return self.my_move


class CyclePlayer(Player):

    def move(self):
        if self.cyclecount == 0:
            return moves[0]
        if self.cyclecount == 1:
            return moves[1]
        if self.cyclecount == 2:
            return moves[2]
        if self.cyclecount == 3:
            return moves[0]
        if self.cyclecount == 4:
            return moves[1]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_trackscore = 0
        self.p2_trackscore = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'You played {move1}.\nOpponent played {move2}.')
        self.p2.learn(move1)
        if self.p1.beats(move1, move2) is True:
            print('\33[1;31m** PLAYER ONE WINS **\33[m\n')
            self.p1_trackscore += 1
        elif self.p2.beats(move2, move1) is True:
            print('\33[1;31m** PLAYER TWO WINS **\33[m\n')
            self.p2_trackscore += 1
        elif move1 == move2:
            print('\33[1;31m** TIE **\33[m\n')
        self.p2.reflectcount += 1
        self.p2.cyclecount += 1

    def play_game(self):
        self.p1_trackscore = 0
        self.p2_trackscore = 0
        self.p2.cyclecount = 0
        print('\33[1;31mGame start!\33[m')
        for round in range(5):
            print(f'Round {round} --')
            self.play_round()
        print('-----------------------------------')
        print('\033[31;1;4mGame over!\033[0m')
        print(f'\033[31;1;4mFINAL SCORE: Player One {self.p1_trackscore}, '
              f'Player Two: {self.p2_trackscore}\033[0m')
        if self.p1_trackscore > self.p2_trackscore:
            print('\033[31;1;4mPlayer One is the Winner!!!\033[0m')
        elif self.p2_trackscore > self.p1_trackscore:
            print('\033[31;1;4mComputer Wins!! Three cheers for AI!!!\033[0m')
        else:
            print('\033[31;1;4mThe match is a tie!!!\033[0m')
        print('-----------------------------------')
        prompt = "Would you like to play again?"
        prompt += " \nHit the return key to play another round"
        prompt += "\nOtherwise, enter 'quit' to end the game. "
        play_again = input(prompt).lower()
        if play_again == 'quit':
            print('Goodbye! Thanks for playing!')
        else:
            game.play_game()


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
