import sys

FOLDER = "folder"
FILE = "file"
SEPARATOR = "/"

def calcFolderSize(tree, path = "", folder = "/"):
  folderIndex = -1
  for index, item in enumerate(tree):
    if item["path"] == path and item["name"] == folder:
      folderIndex = index
      break

  for index, item in enumerate(tree):
    if item["path"] == path + folder:
      if item["type"] == FILE:
        tree[folderIndex]["size"] = tree[folderIndex]["size"] + item["size"]
      else:
        tree[folderIndex]["size"] = tree[folderIndex]["size"] + calcFolderSize(tree, item["path"], item["name"])
  return tree[folderIndex]["size"]

def buildTree(input):
  path = ""
  tree = [{ "type": FOLDER, "path": path, "name": SEPARATOR, "size": 0 }]
  for i, _ in enumerate(input):
    if input[i][0:4] == "$ cd":
      # change folder
      folder = input[i].replace("$ cd ", "")
      if folder == "..":
        path = path[0:path.rindex(SEPARATOR)]
        path = path[0:path.rindex(SEPARATOR)]
        path = path + SEPARATOR
      else:
        path = folder if folder == SEPARATOR else path + folder + SEPARATOR
    elif input[i][0:4] == "$ ls":
      # list folder - nothing to do
      path = path
    elif input[i][0:3] == "dir":
      # folder
      tree.append({
        "type": FOLDER,
        "path": path,
        "name": input[i].replace("dir ", "") + SEPARATOR,
        "size": 0,
      })
    else:
      # file
      [size, name] = input[i].split(" ")
      tree.append({ "type": FILE, "path": path, "name": name, "size": int(size) })
  return tree
  
def process(file_name):
  # Read file
  file = open(file_name, "r")
  content = file.read()
  file.close()
  input = content.splitlines()
  # Process input
  tree = buildTree(input)
  calcFolderSize(tree)
  sum = 0
  for item in tree:
    if item["type"] == FOLDER and item["size"] <= 100000:
      sum = sum + item["size"]
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