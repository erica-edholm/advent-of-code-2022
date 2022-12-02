import unittest

from solvers import day2

INPUT_DATA = ['A Y', 'B X', 'C Z']


class TestDay2(unittest.TestCase):
    def test_solve_part_1(self):
        expected_solution = 15
        solution = day2.solve_part_1(INPUT_DATA)
        self.assertEqual(expected_solution, solution)

    def test_solve_part_2(self):
        expected_solution = 12
        solution = day2.solve_part_2(INPUT_DATA)
        self.assertEqual(expected_solution, solution)
