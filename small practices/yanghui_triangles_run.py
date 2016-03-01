def triangles(maxt=1):
    t=[]
    while True:
        k=[]
        for x in range(len(t)+1):
            if x<len(t) and x!=0: 
                k.append(t[x-1]+t[x])
            else:
                k.append(1)
        t=k
        yield k
    i=0
    for i in range(10):
        triangles()

