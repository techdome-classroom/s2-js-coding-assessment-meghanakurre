def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        int: The sum of the numbers.
    """
    return sum(numbers)

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The average of the numbers.
    """
    return sum(numbers) / len(numbers)

# Test the functions
numbers = [1, 2, 3, 4, 5]
print("Sum:", calculate_sum(numbers))
print("Average:", calculate_average(numbers))


(link unavailable)

def find_max(numbers):
    """
    Find the maximum number in a list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        int: The maximum number.
    """
    return max(numbers)

def find_min(numbers):
    """
    Find the minimum number in a list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        int: The minimum number.
    """
    return min(numbers)

# Test the functions
numbers = [1, 2, 3, 4, 5]
print("Max:", find_max(numbers))
print("Min:", find_min(numbers))


(link unavailable)

import unittest
from program1 import calculate_sum, calculate_average

class TestProgram1(unittest.TestCase):
    def test_calculate_sum(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_sum(numbers), 15)

    def test_calculate_average(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_average(numbers), 3)

if __name__ == "__main__":
    unittest.main()


(link unavailable)

import unittest
from program2 import find_max, find_min

class TestProgram2(unittest.TestCase):
    def test_find_max(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(find_max(numbers), 5)

    def test_find_min(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(find_min(numbers), 1)

if __name__ == "__main__":
    unittest.main()


Run the test scripts using:


bash
python (link unavailable)
python (link unavailable)


If all tests pass, your programs are working correctly.

Commit and push your code to the repository:


bash
git add .
git commit -m "Completed Python coding assessment"
git push
