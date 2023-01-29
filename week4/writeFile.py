numbers = ['one', 'two', 'three', 'four']

file_name = 'numbers.txt'
try:
    with open(file_name, 'w') as number_file: # w for write mode, a for append
        for n in numbers:
            number_file.write(n + ' ')
except OSError:
    print('Erro writing to file. ')