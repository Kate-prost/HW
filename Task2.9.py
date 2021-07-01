
def cir(a,b,c ):
    if a > 0 or b > 0 or c > 0:
        if a + b <= c and a + c <= b and b + c <= a:
            print("Треугольник не существует")
        elif a != b and a != c and b != c:
            print("Разносторонний")
        elif a == b == c:
            print("Равносторонний")
        else:
            print("Равнобедренный")

cir(22,13,18)