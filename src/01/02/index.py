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

  # Find top 3
  max = []
  for index, value in enumerate(elves):
    if index < 3:
      max.append(value)
    else:
      # sort to find the smallest number in max
      max = sorted(max)
      # replace with new value if greater than the smallest in max
      if value > max[0]: max[0] = value

  # Return sum of top 3
  sum = 0
  for item in max:
    sum = sum + item
  return sum

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