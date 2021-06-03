# Finding Text at file
import os.path
import sys

def Isfile(file):
    if os.path.isfile(file):
        return 1
    else:
        return -1
def Isdir(path):
    if os.path.isdir(path):
        return 1
    else:
        return -1
def FindFile(path, text):
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
def FindDir(path, text):
    isdir = Isdir(path)
    if isdir == -1:
        return "0"
    # 21/6/4: FindDir을 추가해요
def TextInput():
    return sys.argv[1]
def PathInput():
    return sys.argv[2]

text = TextInput()
path = PathInput()
if path.find("."):
    print(FindFile(path, text))
else:
    print(FindDir(path, text))
