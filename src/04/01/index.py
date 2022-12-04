import sys

def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()
  # Process input
  count = 0
  for i in range(0, len(input)):
    # Get sections
    [first, second] = input[i].split(',')
    [a, b] = first.split('-')
    [c, d] = second.split('-')
    # Contained?
    if (
      (int(a) <= int(c) and int(b) >= int(d)) or
      (int(c) <= int(a) and int(d) >= int(b))
    ):
      count = count + 1
  return count

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