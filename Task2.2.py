a = [21, 55, 2, 11, 3, 76, 243, 1, 3468, 0, 34, 1]
def min():
    min_numA = a[0]
    for i in range(len(a)):
        if a[i] <= min_numA:
            min_numA = a[i]
    print(min_numA)

    max_num = a[0]
    for i in range(len(a)):
        if a[i] >= max_num:
            max_num = a[i]
    print(max_num)
min()