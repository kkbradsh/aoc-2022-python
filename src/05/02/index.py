import sys

def processStacks(stacks, instructions):
  # Process instructions
  for [move, fromStack, toStack] in instructions:
    fromIndex = int(fromStack) - 1
    toIndex = int(toStack) - 1
    crates = stacks[fromIndex][0:int(move)]
    stacks[fromIndex] = stacks[fromIndex][int(move):]
    stacks[toIndex] = crates + stacks[toIndex]
  
def parseStacks(stacks, line):
  SECTION_LENGTH = 4
  # first time through
  if len(stacks) == 0:
    for i in range(0, len(line), SECTION_LENGTH):
      stacks.append([])
  # each time through
  for i in range(0, len(line), SECTION_LENGTH):
    crate = line[i + 1]
    if crate >= "A" and crate <= "Z":
      stacks[int(i / SECTION_LENGTH)].append(crate)

def parseInstructions(instructions, line):
  [move, fromStack, toStack] = line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
  instructions.append([move, fromStack, toStack])

def parseInput(input):
  stacks = []
  instructions = []
  doneWithStacks = False
  for line in input:
    if line == '':
      doneWithStacks = True
    elif not doneWithStacks:
      parseStacks(stacks, line)
    else:
      parseInstructions(instructions, line)
  return [ stacks, instructions ]

def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()
  # Process input
  [ stacks, instructions ] = parseInput(input)
  processStacks(stacks,instructions)
  # return top of the stacks
  top = ""
  for stack in stacks:
    top = top + stack[0]
  return top

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