import sys

def scoreUp(input, x, y):
  height = input[y][x]
  score = 0
  for yU in range(y - 1, -1, -1):
    nextHeight = input[yU][x]
    if nextHeight < height:
      score = score + 1
    elif nextHeight >= height:
      score = score + 1
      break
  return score

def scoreDown(input, x, y):
  height = input[y][x]
  score = 0
  for yD in range(y + 1, len(input)):
    nextHeight = input[yD][x]
    if nextHeight < height:
      score = score + 1
    elif nextHeight >= height:
      score = score + 1
      break
  return score

def scoreLeft(input, x, y):
  height = input[y][x]
  score = 0  
  for xL in range(x - 1, -1, -1):
    nextHeight = input[y][xL]
    if nextHeight < height:
      score = score + 1
    elif nextHeight >= height:
      score = score + 1
      break
  return score

def scoreRight(input, x, y):
  height = input[y][x]
  score = 0
  for xR in range(x + 1, len(input[y])):
    nextHeight = input[y][xR]
    if nextHeight < height:
      score = score + 1
    elif nextHeight >= height:
      score = score + 1
      break
  return score
def findMaxScore(input):
  max = 0
  for y in range(0, len(input)):
    for x in range(0, len(input[y]) -1):
      score = scoreUp(input, x, y) * scoreRight(input, x, y) * scoreDown(input, x, y) * scoreLeft(input, x, y)
      if score > max: max = score
  return max

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
  return findMaxScore(map)

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