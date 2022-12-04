import unittest

from index import process

class TestProcess(unittest.TestCase):
  def test_process(self):
    # Arrange
    expected = 4
    # Act
    actual = process("./test.txt")
    # Assert
    self.assertEqual(actual, expected)

  def test_final_process(self):
    # Arrange
    expected = 921
    # Act
    actual = process("./final.txt")
    # Assert
    self.assertEqual(actual, expected)    