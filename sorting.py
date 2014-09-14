f = open("words",'r').readlines()
l = {}
for a in f:
    k = a.split(":")
    l[k[0]] = k[1]

keylist = l.keys()
keylist.sort(lambda x,y: cmp(len(y),len(x)))

for a in keylist:
    print a+":"+l[a]
    open("words2.sorted",'a').write(a+":"+l[a])
    
