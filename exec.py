# Finding Text at file
import os.path
import sys

def Isfile(file):
    if os.path.isfile(file):
        return 1
    else:
        return -1
def Find(path, text):
    isfile = Isfile(path)
    if isfile == -1:
        return "0"
    file = open(path, "rb")
    load = file.read() # Bytes load
    file.close()
    read  = load.decode(encoding="utf-8") # Bytes -> Str
    if read.find(text) == -1:
        return -1  # Path 파일에 일치하는  text는 없어요
    else:
        return 1 # 있어요
def TextInput():
    return sys.argv[1]
def PathInput():
    return sys.argv[2]

text = TextInput()
path = PathInput()
print(Find(path, text))
