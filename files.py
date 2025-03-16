def readFile(filePath) :
  with open(filePath, "r") as file:
    textFile = file.read()
    print(textFile)
    return textFile

def writeFile(filePath, text) :
  with open(filePath, "w") as file:
    file.write(text)

def addTextToFile(filePath, text) :
  with open(filePath, "a") as file:
    file.write(text)

path = "testWrite.txt"
# readFile(path)
# writeFile(path, """
# Será que vai subistituir ?
# """)

# addTextToFile(path, """
# Agora adiciona ?
# """)

text = readFile(path)
arrText = text.split()
print(arrText)
print(",".join(arrText))
