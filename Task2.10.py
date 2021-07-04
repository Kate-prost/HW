a = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42,'DD']
b = []

a.remove(False)
a.remove(False)
def lst():
    for i in a:
        if isinstance(i, int):
            b.append(i)
        elif isinstance(i, float):
            b.append(i)
    print(sorted(b))

lst()
