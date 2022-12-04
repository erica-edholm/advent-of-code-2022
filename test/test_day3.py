import unittest

from solvers import day3

INPUT_DATA = ['vJrwpWtwJgWrhcsFMMfFFhFp',
              'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
              'PmmdzqPrVvPwwTWBwg',
              'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
              'ttgJtRGJQctTZtZT',
              'CrZsJsPPZsGzwwsLwLmpwMDw']


class TestDay3(unittest.TestCase):
    def test_solve_part_1(self):
        expected_solution = 157
        solution = day3.solve_part_1(INPUT_DATA)
        self.assertEqual(expected_solution, solution)

    def test_solve_part_2(self):
        expected_solution = 70
        solution = day3.solve_part_2(INPUT_DATA)
        self.assertEqual(expected_solution, solution)
