from datetime import datetime

def tim(func):
    def wr():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wr

@tim
def probDate():
    l = [c for c in range(100000) if c != 1 ]
    return l

probDate()