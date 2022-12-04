import importlib

import click

from solvers import day1, day2, day3
from utils import fetch_input, print_solution


@click.group()
def main():
    pass


@click.command(help='Solution for any given day')
@click.option('--day', required=True, type=click.INT)
def solution(day: int):
    try:
        day_solution = importlib.import_module(f'solvers.day{day}')
        data = fetch_input(day)
        print_solution(1, day_solution.solve_part_1(data))
        print_solution(2, day_solution.solve_part_2(data))
    except ModuleNotFoundError:
        raise click.UsageError(f'Could not find solution for day {day}. Probably it\'s not implemented yet')


main.add_command(solution)

if __name__ == '__main__':
    main()
