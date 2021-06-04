# Finding Text at file
import os.path
import sys
import os

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
        return 0
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
        return 0
    l  = os.listdir(path) # Directroy read
    leng = len(l)
    for i in range(1, leng+1):
        i -= 1 # list
        name = path + "/" + l[i]  # Full name # Basics
        file = open(name, "rb")
        load = file.read()
        file.close()
        read  = load.decode(encoding="utf-8") # Bytes -> Str
        if read.find(text) == -1:
            return -1
        else:
            return "1\n%s"%name # file name을 반환해요
def TextInput():
    return sys.argv[1]
def PathInput():
    return sys.argv[2]
def ManHelp():
    helpfile = "doc/help.md"
    isfile = Isfile(helpfile)
    if isfile == -1:
        print("Error: No help.md file")
        return -1
    file = open(helpfile, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8"))
text = TextInput()
if text == "-h" or "--help":
    ManHelp()
    sys.exit(0)
path = PathInput()
if len(sys.argv) > 3:
    sys.exit(1)
if path.find(".") == -1: # Dir
    dir = FindDir(path, text)
    if dir == -1:
        pass
    else:
        print(dir)
else: # File
    print(FindFile(path, text))    
