import sys

def sumPriorities(input):
  priorities = []
  for i in range(0, len(input), 3):
    # Get compartments
    compartment1 = input[i + 0]
    compartment2 = input[i + 1]
    compartment3 = input[i + 2]
    # Find priorities
    common12 = ''
    for char in compartment1:
      if char in compartment2 and not char in common12:
        common12 = common12 + char
    common = ''
    for char in common12:
      if char in compartment3 and not char in common:
        common = common + char    
    priorities.append(common)

  # Sum priorities
  # ascii value of 'A' is 65, priorities of A-Z is 27 - 52
  # ascii value of 'a' is 97, a-z is 1 - 26
  sum = 0
  for item in priorities:
    if item == item.lower():
      sum = sum + ord(item) - 97 + 1
    else:
      sum = sum + ord(item) - 65 + 27
  return sum  

def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()
  # Sum Priorities
  return sumPriorities(input)

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