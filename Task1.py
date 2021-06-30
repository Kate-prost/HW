f = open("Fu.txt")
content = f.read()
content = content.split("\n")
people = []
def oooor():
    srednia = 0
    for line in content:
        """В цикле разбивается строка и записывается в список"""
        line = line.split(" ")
        people.append([line[0], line[1], int(line[2])])
    print("Ниже 3 баллов:")
    for p in people:
        """В этом цикле проходим по созданному списку, считываем среднюю и вычисляем у кого оценка ниже 3"""
        srednia += int(p[2])
        if p[2] < 3:
            print(f"{p[0]} {p[1]}: {p[2]}")
            srednia /= len(people)
    print(f"Среднее значение:", srednia)
print(oooor())
"""Не забуть закрыть файл!!"""
f.close()
