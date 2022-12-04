import unittest

from solvers import day3, day4

INPUT_DATA = ['2-4,6-8',
              '2-3,4-5',
              '5-7,7-9',
              '2-8,3-7',
              '6-6,4-6',
              '2-6,4-8']


class TestDay4(unittest.TestCase):
    def test_solve_part_1(self):
        expected_solution = 2
        solution = day4.solve_part_1(INPUT_DATA)
        self.assertEqual(expected_solution, solution)

    def test_solve_part_2(self):
        expected_solution = 4
        solution = day4.solve_part_2(INPUT_DATA)
        self.assertEqual(expected_solution, solution)
