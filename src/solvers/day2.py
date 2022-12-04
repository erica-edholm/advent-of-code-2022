from enum import Enum, auto

import click

from utils import fetch_input, print_solution


class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def list(cls):
        return list(map(lambda c: c, cls))


WINNING_MOVES = {
    Moves.ROCK: Moves.SCISSORS,
    Moves.SCISSORS: Moves.PAPER,
    Moves.PAPER: Moves.ROCK
}

TO_OPPONENT_MOVE = {
    'A': Moves.ROCK,
    'B': Moves.PAPER,
    'C': Moves.SCISSORS
}

TO_YOUR_MOVE = {
    'X': Moves.ROCK,
    'Y': Moves.PAPER,
    'Z': Moves.SCISSORS
}


def solve_part_1(data):
    points = 0
    for strategy in data:
        first_move, second_move = strategy.split(' ')
        opponent_move = TO_OPPONENT_MOVE[first_move]
        your_move = TO_YOUR_MOVE[second_move]
        points += __calculate_points_by_moves(opponent_move, your_move)
    return points


def solve_part_2(data):
    points = 0
    for strategy in data:
        move, result = strategy.split(' ')
        opponent_move = TO_OPPONENT_MOVE[move]
        valid_moves = Moves.list()
        if result == 'X':
            your_move = WINNING_MOVES[opponent_move]
        elif result == 'Y':
            your_move = opponent_move
        elif result == 'Z':
            valid_moves.remove(opponent_move)
            valid_moves.remove(WINNING_MOVES[opponent_move])
            your_move = valid_moves.pop()
        else:
            raise ValueError(f'Not a valid result: {result}')
        points += __calculate_points_by_moves(opponent_move, your_move)
    return points


def __calculate_points_by_moves(opponent_move, your_move):
    points = your_move.value
    if opponent_move == your_move:
        points += 3
    if WINNING_MOVES[your_move] == opponent_move:
        points += 6
    return points
