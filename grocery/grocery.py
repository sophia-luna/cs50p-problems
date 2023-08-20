glist={}
while True:
    try:
        item=input().upper()
    except EOFError:
        break
    else:
        if item in glist:
            glist[item]+=1
        else:
            glist[item]=1

for i in sorted(glist.keys()):
    print(glist[i],i)