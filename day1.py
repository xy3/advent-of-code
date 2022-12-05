import sys

x = sys.stdin.read()
groups = x.split("\n\n")

b = lambda n: int(n.strip())
o = lambda g: sum(map(b,g.split("\n")))
print(sum(sorted(map(o, groups))[-3:]))