import unittest

from solvers import day1

INPUT_DATA = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']


class TestDay1(unittest.TestCase):

    def test_solve_part_1(self):
        expected_solution = 24000
        solution = day1.solve_part_1(INPUT_DATA)
        self.assertEqual(expected_solution, solution)

    def test_solve_part_2(self):
        expected_solution = 45000
        solution = day1.solve_part_2(INPUT_DATA)
        self.assertEqual(expected_solution, solution)
