f = open("xyz.txt")
c = f.read()
def YZ():
    countY = 0
    countZ = 0
    for i in c:
        if i == 'y':
            countY += 1
        elif i == 'z':
            countZ +=1
    print(f"Y = {countY}, Z = {countZ}")
YZ()
