import unittest

from index import process

class TestProcess(unittest.TestCase):
  def test_process(self):
    # Arrange
    expected = 8
    # Act
    actual = process("./test.txt")
    # Assert
    self.assertEqual(actual, expected)
