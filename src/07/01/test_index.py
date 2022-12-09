import unittest

from index import process

class TestProcess(unittest.TestCase):
  def test_process(self):
    # Arrange
    expected = 95437
    # Act
    actual = process("./test.txt")
    # Assert
    self.assertEqual(actual, expected)
