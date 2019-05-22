#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""

import random

moves = ['rock', 'paper', 'scissors']

class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)

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
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if self.p1.beats(move1, move2) is True:
            print('** PLAYER ONE WINS **')
            self.p1_trackscore += 1
        elif self.p2.beats(move2, move1) is True:
            print('** PLAYER TWO WINS **')
            self.p2_trackscore += 1
        elif move1 == move2:
            print('** TIE **')

    def play_game(self):
        print('Game start!')
        for round in range(5):
            print(f'Round {round} --')
            self.play_round()
        print('Game over!')
        print(f'FINAL SCORE: Player One {self.p1_trackscore}, '
             f'Player Two: {self.p2_trackscore}')


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
