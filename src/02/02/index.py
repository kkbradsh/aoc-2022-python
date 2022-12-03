import sys

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

LOSE = 0
DRAW = 3
WIN = 6

ABC = {
  "A": ROCK,
  "B": PAPER,
  "C": SCISSORS,
}

XYZ = {
  "X": LOSE,
  "Y": DRAW,
  "Z": WIN,
}

SCORE = {
  ROCK: 1,
  PAPER: 2,
  SCISSORS: 3,
}

RUBRIC = {
  ROCK: {
    ROCK: DRAW,
    PAPER: WIN,
    SCISSORS: LOSE,
  },
  PAPER: {
    ROCK: LOSE,
    PAPER: DRAW,
    SCISSORS: WIN,
  },
  SCISSORS: {
    ROCK: WIN,
    PAPER: LOSE,
    SCISSORS: DRAW,
  },
}

def playGame(input):
  score = 0
  for i in range(0, len(input)):
    [theirEncodedPlay, myEncodedOutcome] = input[i].split()
    theirPlay = ABC[theirEncodedPlay]
    myOutcome = XYZ[myEncodedOutcome]
    myPlay = ''
    for play in RUBRIC[theirPlay]:
      if RUBRIC[theirPlay][play] == myOutcome:
        myPlay = play
        break
    score = score + SCORE[myPlay] + myOutcome
  return score
  
def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()

  # Play game
  return playGame(input)

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