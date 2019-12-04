#bruteforce... (part2)
cnt = 0
for i in range(245182,790572):
    req=True
    s=str(i)
    for x in range(len(s)-1):
        if s[x] > s[x+1]:
            req=False
    if not req:
        continue
    #else
    req=False
    x=0
    while x < 5:
        if s[x] == s[x+1]:
            req=True
            if x+2 < 6 and s[x+2] == s[x]:
                req=False
                x+=1
                if x+2 < 6 and s[x+2] == s[x]:
                    x+=1
                if x+2 < 6 and s[x+2] == s[x]:
                    x+=1
                if x+2 < 6 and s[x+2] == s[x]:
                    x+=1
            else:
                break
            x+=2
        else:
            x+=1
    if req:
        cnt+=1
print (cnt)

