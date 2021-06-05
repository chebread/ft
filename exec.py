# Finding Text at file and directory
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

def FindDir(path, text): # tests/jotting
    if Isdir(path) == -1:
        return 0 # No directory
    dir_list = os.listdir(path)

    if '.git' in dir_list:
        dir_list.remove('.git')
    if '.github' in dir_list:
        dir_list.remove('.github')
    if '.DS_Store' in dir_list:
        dir_list.remove('.DS_Store')
    leng = len(dir_list) # value
    exts = ''
    ext = ''
    for i in range(1, leng):
        name = "".join(dir_list[i-1])
        file = path + '/' + dir_list[i-1]
        #print("name: %s"%name)
        #print("file: %s"%file)
        if name.find(".") != -1: # file
            f = open(file, "rb")
            load = f.read()
            f.close()
            read = load.decode(encoding="utf-8")
            find = read.find(text) # -1 or 1~~
            if find != -1: # 1
                ext = "%s\n"%file
                exts = exts + ext
            if i+1 == leng:
                if ext == '':
                    return -1 # No file in dir
                #print("exts: %s"%)
                return exts
        else: # dir
            dir = FindDir(file, text)
def TextInput():
    return sys.argv[1]

def PathInput():
    return sys.argv[2]

def NowDir():
    return os.path.dirname(os.path.abspath(__file__))
def ManHelp():
    now = NowDir()
    help_file = now + "/doc/help.md"
    isfile = Isfile(help_file)
    if isfile == -1:
        print("Error: No help.md file")
        return -1
    file = open(help_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8")) # Prints
def ManVer():
    now = NowDir()
    ver_file = now + "/doc/version.md"
    isfile = Isfile(ver_file)
    if isfile == -1:
        print("Error: No version.md file")
        return -1
    file = open(ver_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8")) # Prints
def ManIndexErrorHelp(flag):
    print("error: No '%s' flags"%flag)
    now = NowDir()
    err_file = now + "/doc/error_help.md"
    isfile = Isfile(err_file)
    if isfile == -1:
        print("Error: No error_help.md file")
        return -1
    file = open(err_file, "rb")
    load = file.read()
    file.close()
    print(load.decode(encoding="utf-8")) # Prints
try:
    text = '' # NameError 방지해요
    text = TextInput()
    # Flags
    if (text.find("-h")==0 or text.find("--h")==0):
        ManHelp()
        sys.exit(0)
    if (text.find("-v")==0 or text.find("-V")==0 or text.find("--v")==0):
        ManVer()
        sys.exit(0)
    path = PathInput()
    if len(sys.argv) > 3:
        sys.exit(1) # 비정상 종료에요
    # Options
    if path == '*':
        path = os.getcwd()
        print("getcwd: %s"%path)
    dir = FindDir(path, text)
    if dir == -1: # -1 of dir
        print(-1)
    elif dir == 0: # 0 of dir or file: 1 or -1
        file = FindFile(path, text)
        if file == 0:
            print(0) # file or dir of No find value
        else:
            print(file) # file of 1 or -1
    else: # 1 of dir
        print(1)
        print(dir)
except IndexError:
   ManIndexErrorHelp(text)
