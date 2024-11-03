import unittest
from math_quiz import generate_random_number, generate_random_operation, calculate_operation


class TestMathGame(unittest.TestCase):

    # Test if random numbers generated are within the specified range
    def test_generate_random_number(self):       
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    # Test if the operations are generated correctly
    def test_generate_random_operation(self):        
        for _ in range(100):
            operation = generate_random_operation()
            self.assertTrue(operation in ['+', '-', '*'])

    # Test if output from calculations are equal to the actual value
    def test_calculate_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 3, '*', '3 * 3', 9),
                (9, 5, '+', '9 + 5', 14),
                (7, 8, '*', '7 * 8', 56)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = calculate_operation(num1, num2, operator)
                self.assertTrue(PROBLEM == expected_problem and 
                                ANSWER == expected_answer)

if __name__ == "__main__":
    unittest.main()
