def line(s, t):
    x = float(t[:t.index(';')])
    y = float(t[t.index(';') + 1:])
    k = float(s[:s.index('x')])
    b = float(s[s.index('x') + 1:])
    print((k * x + b) == y)
