a = [4,2,6,'23',8,'one',234]
b = [76,'one','lol',987,5,2,4]
c = []
def arr():
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
    print(c)
arr()