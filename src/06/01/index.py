import sys

def findMarker(line):
  MARKER_LENGTH = 4
  for i in range(MARKER_LENGTH, len(line)):
    markers = line[i-MARKER_LENGTH:i]
    markerSet = set(markers)
    if len(markerSet) == len(markers):
      return i
  
def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()
  # Process input
  return findMarker(input[0])

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