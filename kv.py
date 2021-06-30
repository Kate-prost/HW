def solver(a,b,c):
    d =(b**2)-4 * a * c
    if d == 0:
        x = -b / 2 * a
        return x
    elif d > 0:
        x1 = (-b + d ** 0,5)/ 2 * a
        x2 = (-b - d ** 0,5)/ 2 * a
        return (x1,x2)
    else:
        return ("Нет действующих корней")
print(solver(2,5,8))