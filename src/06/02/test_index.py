import unittest

from index import findMarker

class TestFindMarker(unittest.TestCase):
  def test_findmarker01(self):
    # Arrange
    expected = 19
    # Act
    actual = findMarker("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    # Assert
    self.assertEqual(actual, expected)

  def test_findmarker02(self):
    # Arrange
    expected = 23
    # Act
    actual = findMarker("bvwbjplbgvbhsrlpgdmjqwftvncz")
    # Assert
    self.assertEqual(actual, expected)

  def test_findmarker03(self):
    # Arrange
    expected = 23
    # Act
    actual = findMarker("nppdvjthqldpwncqszvftbrmjlhg")
    # Assert
    self.assertEqual(actual, expected)

  def test_findmarker04(self):
    # Arrange
    expected = 29
    # Act
    actual = findMarker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    # Assert
    self.assertEqual(actual, expected)

  def test_findmarker04(self):
    # Arrange
    expected = 26
    # Act
    actual = findMarker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    # Assert
    self.assertEqual(actual, expected)
