# Finding Text at file and directory
import os.path
import sys
import os

# 전역 변수
x, y, p = 0, 0, 0
exts = []

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
def Table(text):
    n = len(text)
    table = [0] * n
    m = 0
    for i in range(1, n):
        while m > 0 and text[i] != text[m]:
            m = table[m-1]
        if text[i] == text[m]:
            m += 1
            table[i] = m
    return table
def Find(target, text):
    c = 0 # count
    m = 0
    if text == '':
        text = ' '
    table = Table(text)
    for i in range(len(target)):
        while m > 0 and target[i] != text[m]:
            m = table[m-1]
        if target[i] == text[m]:
            m += 1
            if m == len(text):
                c += 1 # conut += 1
                m = table[m-1]
    return c
def FindFile(path, text):
    isfile = Isfile(path)
    if isfile == -1:
        return 0
    file = open(path, "rb")
    load = file.read() # Bytes load
    file.close()
    read = load.decode(encoding="utf-8") # Bytes -> Str
    if Find(read, text) > 0:
        return 1
    else:
       return -1
def FindDir(path, text):
    global x
    try:
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
        for i in range(1, leng+1):
            name = "".join(dir_list[i-1])
            file = path + '/' + dir_list[i-1]
            if name.find(".") != -1: # file
                find = FindFile(file, text)
                if find != -1:
                    x = 0 + 1
                    ext = "%s\n"%file # \n을 추가해서 "".join(exts)해도 줄 바꿈이 괜찮은거에요
                    exts.append(ext)
            else: # dir
                dir = FindDir(file, text)
        if x == 0:
            return -1 # 파일에 찾는 문자열이 없다면
        return "".join(exts) # No return of value (1: extant)
    except UnicodeDecodeError: # 만약 못읽는 파일이 나오면 못읽는 파일은 읽지 않아요
        pass
def TextInput():
    return sys.argv[1]
def PathInput():
    return sys.argv[2]
def NowDir():
    return os.path.dirname(os.path.abspath(__file__))
def TextLower(text):
    return text.lower()
def TextUpper(text):
    return text.upper()
def ManHelp():
    ManVer()
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
    print(load.decode(encoding="utf-8")) # Print
def Flags():
    global text
    cp_text = text # 복사본으로 이용해요
    for i in range(1, 3):
        if i == 1:
            cp_text = TextLower(cp_text)
        else:
            cp_text = TextUpper(cp_text)
        if (cp_text.find('-h')==0 or cp_text.find('--h')==0):
            ManHelp()
            return sys.exit(0)
        if (cp_text.find('-v')==0 or cp_text.find('--v')==0):
            ManVer()
            return sys.exit(0)
def Opptions():
    global path
    if (path.find("!")==0 or path.find("*")==0):
        path = os.getcwd()
def Print(text, path):
    global dir, y
    for i in range(1, 3):
        if i == 1:
            text = TextLower(text)
        else:
            text = TextUpper(text)
        dir = FindDir(path, text)
        if dir == -1: # -1 of dir
            y = 3
        elif dir == 0: # 0 of dir or file: 1 or -1
            file = FindFile(path, text)
            if file == 0:
                y = 2
                #f = 0 + file
            else: # file of 1 or -1
                y = 4
        else: # 1
            y = 1
def PrintValue():
    global dir, path
    if y == 1:
        dir = dir.split() # Str -> List
        set_ = set(dir) # 순서가 바뀌어요
        dir = list(set_)
        dir.sort()
        leng = len(dir)
        for i in range(1, leng+1):
            print("".join(dir[i-1]))
        print(i)
        # 1 말고 파일 개수를 출력해줘요
    if y == 2:
        print(0)
    if y == 3:
        print(-1)
    if (y==4):
        print(1)
try:
    text, path = ' ', ' ' # NameError 방지해요
    text = TextInput()
    # Flags
    Flags()
    path = PathInput()
    if len(sys.argv) > 3: # 다중 인자 입력 방지
        sys.exit(1)
    # Opptions
    Opptions()
    # Find
    Print(text, path)
    # Print value
    PrintValue()
except IndexError: # sys.argv의 인자가 충분히 제공 되지 않았을때
    if (text.find("-")==0):
        ManIndexErrorHelp(text)
    else:
        path = os.getcwd()
        Print(text, path)
        PrintValue()
