# Write a warships game with field 5x5
from prettytable import PrettyTable
from random import randint

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def sea_table(ocean):
    mytable = PrettyTable()
    mytable.title = bcolors.OKBLUE + 'Sea Fight' + bcolors.ENDC
    mytable.add_column(' ', ['1', '2', '3', '4', '5'])
    mytable.add_column('1', ocean[0])
    mytable.add_column('2', ocean[1])
    mytable.add_column('3', ocean[2])
    mytable.add_column('4', ocean[3])
    mytable.add_column('5', ocean[4])
    print(mytable)

def play():
    ocean = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    random_row = randint(0, 4)
    random_col = randint(0, 4)
    count = 1
    sea_table(ocean)
    while True:
        try:
            user_col = int(input('Guess column ')) - 1
            user_row = int(input('Guess row ')) - 1
            if user_row == random_row and user_col == random_col:
                ocean[random_col][random_row] = bcolors.FAIL + 'W' + bcolors.ENDC
                print('Yes')
                sea_table(ocean)
                break
            else:
                ocean[user_col][user_row] = bcolors.WARNING + 'X' + bcolors.ENDC
                print('Ship is not here')
                sea_table(ocean)
                print('It was try #' + str(count))
                count += 1
            if count == 6:
                print(f'Ship was here: col: {random_col + 1}, row: {random_row + 1}')
                ocean[random_col][random_row] = bcolors.FAIL + 'W' + bcolors.ENDC
                sea_table(ocean)
                break
        except ValueError:
            print('Sorry, invalid number')
            continue
        except IndexError:
            print("Sorry, the number is out of range")
            continue

play()