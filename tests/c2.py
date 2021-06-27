def Lps(p):
    n = len(p)
    table = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and p[i] != p[k]:
            k = table[k - 1]
        if p[i] == p[k]:
            k += 1
            table[i] = k
    return table
def Find(s, p):
    k = 0
    c = 0
    table = Lps(p)
    for i in range(len(s)):
        while k > 0 and s[i] != p[k]:
            k = table[k - 1]
        if s[i] == p[k]:
            k += 1
            if k == len(p):
                c = 1
                k = table[k - 1]
    return c # 0이나 1만 반환되요