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
def FindDir(path, text):
    isdir = Isdir(path)
    if isdir == -1:
        return 0
    l  = os.listdir(path)
    if '.git' in l:
        l.remove('.git')
    if '.DS_Store' in l:
        l.remove('.DS_Store')
    if '.github' in l:
        l.remove('.github')
    leng = len(l) # 6번 돌아요
    print("l: %s"%l)
    ext_dir = ''
    ext = ''
    for i in range(1, leng+1): # all file
        name = "".join(l[i-1]) # 파일을 문자열화 해요
        if name.find('.') != -1: # file # 1
            i -= 1
            file = path + "/" + l[i-1]
            f = open(file, "rb")
            load = f.read()
            f.close()
            read = load.decode(encoding="utf-8")
            find = read.find(text)
            if find != 1: # 1
                ext == ''
                ext = "%s\n"%file
                ext_dir += ext
            if i+1 == leng:
                if ext_dir == '':
                    return -1 # -1
                return ext_dir
        else: # dir # -1
            dir = path + '/' + l[i-1] # dir/dir
            dir2 = FindDir(dir, text) # re-return # file
            print("dir2: %s"%dir2)
        #i -= 1
        #name = path + "/" + l[i]  
        #print("name: %s"%name)
        #isdir2 = Isdir(name)
        #if isdir2 == 1:
        #    dir2 = FindDir(name, text) # dir of file # 1
        #    print(dir2) # -1 at findtext
        #    if dir2== -1: # Value extant
        #        break
        #    else: # 1
        #        extant_dir += dir2 # file
        #file = open(name, "rb")
        #load = file.read()
        #file.close()
        #read  = load.decode(encoding="utf-8") # Bytes -> Str
        #find = read.find(text)
        #if read.find(text) == -1:
        #    #print("0")
        #    pass # 없다면 pass
        #elif read.find(text) != -1:
        #    extant = ''
        #    extant = "%s\n"%name # file name을 반환해요
        #    extant_dir += extant # 값이 차곡차곡 쌓인다
        #if i+1 == leng:
        #    if extant_dir == '':
        #        print("ext: %s"%extant_dir)
        #        return -1
        #    return extant_dir
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
    text = '' # NameError를 방지하기 위한 변수 초기화를 해요
    text = TextInput()
    if (text.find("-h")==0 or text.find("--h")==0):
        ManHelp()
        sys.exit(0)
    if (text.find("-v")==0 or text.find("-V")==0 or text.find("--v")==0):
        ManVer()
        sys.exit(0)
    path = PathInput()
    if len(sys.argv) > 3:
        sys.exit(1)
    if path == '*':
        path = os.getcwd()
    dir = FindDir(path, text)
    if dir == -1:
        print(dir) # -1 :dir
    elif dir == 0:
        file = FindFile(path, text)
        if file == 0:
            print(0) # 0: dir, 0:file
        else:
            print(file) # 1 or -1 :file
    else:
        print(1)
        print(dir) # 1 \n <file...> :dir
except IndexError:
    ManIndexErrorHelp(text)
