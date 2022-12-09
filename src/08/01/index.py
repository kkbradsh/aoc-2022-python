import sys

def isVisibleUp(input, x, y):
  height = input[y][x]
  for yU in range(y - 1, -1, -1):
    if input[yU][x] >= height: return False
  return True

def isVisibleDown(input, x, y):
  height = input[y][x]
  for yD in range(y + 1, len(input)):
    if input[yD][x] >= height: return False
  return True

def isVisibleLeft(input, x, y):
  height = input[y][x]
  for xL in range(x - 1, -1, -1):
    if input[y][xL] >= height: return False
  return True

def isVisibleRight(input, x, y):
  height = input[y][x]
  for xR in range(x + 1, len(input[y])):
    if input[y][xR] >= height: return False
  return True

def findVisible(input):
  # edges
  count = len(input) * 2 + len(input[0]) * 2 - 4
  # inner
  for y in range(1, len(input) - 1):
    for x in range(1, len(input[y]) -1):
      if (
        isVisibleUp(input, x, y) or
        isVisibleRight(input, x, y) or
        isVisibleDown(input, x, y) or
        isVisibleLeft(input, x, y)
      ):
        count = count + 1
  return count

def parseInput(input):
  map = []
  for i in range(0, len(input)):
    map.append(list(input[i]))
  return map
  
def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()
  # Process input
  map = parseInput(input)
  return findVisible(map)

def main():
  print(process("./final.txt"))

try:
    if len(sys.argv) >= 2:
      function = sys.argv[1]
      globals()[function]()
except IndexError:
    raise Exception("Please provide function name")
except KeyError:
    raise Exception("Function {} hasn't been found".format(function))