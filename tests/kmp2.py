# KMP
def Dup(p): # a
    n = len(p) # 1
    print("len: %s"%n) # 1
    table = [0] * n # 0*n만큼 0 배열을 만들어요
    print("table: %s"%(table))
    j = 0
    for i in range(1, n):
        print("i: %s"%i) # 1
        while j > 0 and p[i] != p[j]: # 일치하지 않는 경우 이 경우를 돌아요
            j = table[j - 1] # 일치했던 접두 접미의 개수 j-1 이에요(인덱스는 0 부터 시작해서요)
        if p[i] == p[j]: # 일치
            j += 1 # j=1 # 문자열 일치 개수 # 1씩 커짐
            table[i] = j # [0,..]에 1을 추가해요
            print("j: %s"%j)
    return table # 1이나 0을 반환해요 # 0

def Kmp(s, p):
    j = 0 # 패턴 인덱스 
    cnt = 0 # 일치 개수 
    table = Dup(p) # [0]
    print("table2: %s"%table)
    for i in range(len(s)): # 2
        print("i2: %s"%i)
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]: # a==a
            j += 1
            if j == len(p): # 일치
                cnt += 1
                j = table[j - 1] # j = 0
    return cnt # 일치 개수를 반환해요

s = input() # abc
p = input() # a
table = Dup(p)
answer = Kmp(s, p)
print(answer)