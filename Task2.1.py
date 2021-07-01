from random import randint
my_list = [randint(1, 100) for i in range(100)]
my_list.sort()
for i in range(0,len(my_list)-1):
               if my_list[i] == my_list[i+1]:
                   print(str(my_list[i]) + ' duplicate')
