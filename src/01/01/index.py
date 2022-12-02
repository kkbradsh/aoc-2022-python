import sys

def parseArrayIntoGroupedSummary(input):
  output = []
  output.append(0)
  for line in input:
    if (line == ""):
      output.append(0)
    else:
      output[len(output) - 1] = output[len(output) - 1] + int(line)
  return output

def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()

  # Sum calories per elf
  elves = parseArrayIntoGroupedSummary(input)

  # Return max
  return max(elves)

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