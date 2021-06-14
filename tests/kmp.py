# KMP
def Dup(p):
    n = len(p)
    table = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1] # 일치했던 접두 접미의 개수 j-1 이에요(인덱스는 0 부터 시작해서요)
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def Kmp(s, p):
    j = 0 # 패턴 인덱스 
    cnt = 0 # 일치 개수 
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            j += 1
            if j == len(p): # 일치
                cnt += 1
                j = table[j - 1]
    return cnt

s = input()
p = input()
table = Dup(p)

answer = Kmp(s, p)
print(answer)
