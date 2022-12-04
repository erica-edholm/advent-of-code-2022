import click

from utils import fetch_input, print_solution


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
