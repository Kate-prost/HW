def three_args(*, var1=123, var2=None, var3='lol'):

    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')

three_args()