l=input().strip();print(l.index("".join([g for g in[l[x-4:x]for x in range(len(l))]if len(set(g))==4][0]))+4)
