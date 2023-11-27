from time import process_time_ns
from random import randint
import matplotlib.pyplot as plt 
from copy import deepcopy

from sorts import comb_sort, binary_tree_sort, merge_sort


MSG = "\n\n      Меню \n\n \
    1. Сортировка расческой \n \
    2. Сортировка бинарным деревом \n \
    3. Сортировка слиянием \n \
    4. Замеры времени \n \
    0. Выход \n\n \
    \
    Выбор: \
    "

EXIT = 0
COMB = 1
TREE = 2
MERGE = 3
TIME = 4

TIMES = 1000
TO_MILISECONDS = 1000

INPUT_KEYBOARD = 1
INPUT_FILE = 0
INPUT_TYPE = 0

FILE = "arr25.csv"


def input_arr_keyboard():
    arr = list()

    nums = 0

    print("Введите массив поэлементно в одной строке (окончание - Enter): ")

    nums = input().split()

    for i in range(len(nums)):
        try:
            arr.append(int(nums[i]))
        except:
            print("Ошибка: введено не число")

    return arr


def input_arr_file():
    f = open(FILE, "r")

    arr = list()

    for line in f:
        try:
            arr.append(int(line))
        except:
            print("Ошибка: введено не число")

    return arr


def input_arr():

    if (INPUT_TYPE):
        arr = input_arr_keyboard()
    else:
        arr = input_arr_file()

    return arr


def get_arr_sorted(size):
    arr = list()

    for i in range(size):
        arr.append(i)

    return arr


def get_arr_down_sorted(size):
    arr = list()

    for i in range(size):
        arr.append(size - i)

    return arr


def get_arr_random(size):
    arr = list()

    for _ in range(size):
        arr.append(randint(0, 1000))

    return arr


def get_arr_by_type(option, size):

    type = "Не определено"

    if (option == 0):

        arr = get_arr_sorted(size)
        type = "Отсортированный "


    elif (option == 1):

        arr = get_arr_down_sorted(size)
        type = "Отсортированный в обратном порядке "

    elif (option == 2):

        arr = get_arr_random(size)
        type = "Случайный "

    return arr, type


def get_process_time(func, arr):
    
    time_res = 0

    for _ in range(TIMES):
        arr_tmp = deepcopy(arr)

        time_start = process_time_ns()
        func(arr_tmp)
        time_end = process_time_ns()

        time_res += (time_end - time_start) / TO_MILISECONDS


    return time_res / TIMES


def test_sort():
    time_comb = []
    time_binary_tree = []
    time_merge = []

    option = int(input("\nВведите тип массива \n(0 - отсортированный, 1 - отсортированный в обратном порядке, 2 - случайный): "))

    # sizes = [10, 50, 100, 200, 300, 400, 500]
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]

    for num in sizes:
        arr, type = get_arr_by_type(option, num)

        time_comb.append(get_process_time(comb_sort, arr))
        time_binary_tree.append(get_process_time(binary_tree_sort, arr))
        time_merge.append(get_process_time(merge_sort, arr))
        print(num)

    print("\n\n" + type + "массив: \n")

    ind = 0

    for num in sizes:
        print(" %4d & %.2f & %.2f & %.2f \\\\ \n \\hline" %(num, \
            time_comb[ind], \
            time_binary_tree[ind], \
            time_merge[ind]
            ))

        ind += 1


    fig1 = plt.figure(figsize=(10, 7))
    plot = fig1.add_subplot()
    plot.plot(sizes, time_comb, label = "Сортировка расческой")
    plot.plot(sizes, time_binary_tree, label="Сортировка бинарным деревом")
    plot.plot(sizes, time_merge, label="Сортировка слиянием")
    plot.semilogy()
    
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики алгоритмов сортировок\n" + type + "массив")
    plt.ylabel("Затраченное время (мс)")
    plt.xlabel("Длина массива")
    
    plt.show()


def main():
    option = -1

    while (option != EXIT):
        option = int(input(MSG))

        if (option == COMB):

            arr = input_arr()
            print(comb_sort(arr))

        elif (option == TREE):

            arr = input_arr()
            print(binary_tree_sort(arr))

        elif (option == MERGE):
            
            arr = input_arr()
            print(merge_sort(arr))

        elif (option == TIME):

            test_sort()


if __name__ == "__main__":
    main()
