import click

from utils import fetch_input, print_solution


@click.command(help='Solution for day 1')
def day1():
    data = fetch_input(1)
    print_solution(1, solve_part_1(data))
    print_solution(2, solve_part_2(data))


def solve_part_1(data):
    sums = __get_calories_sum(data)
    return max(sums)


def solve_part_2(data):
    sums = __get_calories_sum(data)
    return sum(sorted(sums, reverse=True)[:3])


def __get_calories_sum(data):
    sums = []
    current_sum = 0
    for value in data:
        if value == '':
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(value)
    sums.append(current_sum)
    return sums
