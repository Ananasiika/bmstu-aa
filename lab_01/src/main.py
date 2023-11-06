from time import process_time
from random import choice
import matplotlib.pyplot as plt 
import string

from algorythms import damerau_levenshtein_recursive, damerau_levenshtein_cache_recursive, levenshtein_matrix, damerau_levenshtein_matrix


MSG = "\n\n     Меню \n\n \
    1. Расстояние Левенштейна (матрица) \n \
    2. Расстояние Дамерау-Левенштейна (матрица) \n \
    3. Расстояние Дамерау-Левенштейна (рекурсивно) \n \
    4. Расстояние Дамерау-Левенштейна (рекурсивно с кешем) \n \
    5. Замерить времени \n \
    0. Выход \n\n \
    \
    Выбор: \
    "

EXIT = 0
LEV_MAT = 1
DAM_LEV_MAT = 2
DAM_LEV_REC = 3
DAM_LEV_REC_CACHE = 4
TIME =  5

TIMES = 100
TO_MILISECONDS = 1000


def input_data():
    str1 = input("\nВведите 1-ую строку:\t")
    str2 = input("Введите 2-ую строку:\t")

    return str1, str2


def get_random_string(size):
    letters = string.ascii_lowercase

    return "".join(choice(letters) for _ in range(size))


def get_process_time(func, size):
    
    time_res = 0

    for _ in range(TIMES):
        str1 = get_random_string(size)
        str2 = get_random_string(size)

        time_start = process_time()
        func(str1, str2, output = False)
        time_end = process_time()

        time_res += (time_end - time_start)


    return time_res / TIMES

def graph(time_dam_lev_mat, time_dam_lev_rec_cache, time_lev_mat):

    sizes = [i for i in range(1, 101)]

    fig1 = plt.figure(figsize=(10, 7))
    plot1 = fig1.add_subplot()
    plot1.plot(sizes, time_lev_mat, label = "Левенштейн (матрица)")
    plot1.plot(sizes, time_dam_lev_mat, label = "Дамерау-Левенштейн (матрица)")
    plot1.plot(sizes, time_dam_lev_rec_cache, label = "Дамерау-Левенштейн (рекурсивный с кешэм)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")
    
    plt.show() 

def graph_all(time_dam_lev_mat, time_dam_lev_rec, time_dam_lev_rec_cache, time_lev_mat):

    sizes = [i for i in range(1, 11)]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(sizes, time_lev_mat[:10], label = "Левенштейн (матрица)")
    plot.plot(sizes, time_dam_lev_mat[:10], label = "Дамерау-Левенштейн (матрица)")
    plot.plot(sizes, time_dam_lev_rec[:10], label = "Дамерау-Левенштейн (рекурсивный)")
    plot.plot(sizes, time_dam_lev_rec_cache[:10], label = "Дамерау-Левенштейн (рекурсивный с кешэм)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")
    
    plt.show() 

def time_measurement():
    time_lev_mat = []
    time_dam_lev_mat = []
    time_dam_lev_rec = []
    time_dam_lev_rec_cache = []

    for num in range(1, 101):
        time_lev_mat.append(get_process_time(levenshtein_matrix, num))
        time_dam_lev_mat.append(get_process_time(damerau_levenshtein_matrix, num))
        time_dam_lev_rec_cache.append(get_process_time(damerau_levenshtein_cache_recursive, num))

    for num in range(1, 11):
        time_dam_lev_rec.append(get_process_time(damerau_levenshtein_recursive, num))

    print("\n\nЗамер времени для алгоритмов: \n")

    ind = 0

    for num in range(1, 101):
        if num < 11:
            print(" %4d | %.4f | %.4f | %.4f | %.4f \n\n" %(num, \
                time_lev_mat[ind] * TO_MILISECONDS, \
                time_dam_lev_mat[ind] * TO_MILISECONDS, \
                time_dam_lev_rec[ind] * TO_MILISECONDS, \
                time_dam_lev_rec_cache[ind] * TO_MILISECONDS))
        else:
            print(" %4d | %.4f | %.4f |        | %.4f \n\n" %(num, \
                time_lev_mat[ind] * TO_MILISECONDS, \
                time_dam_lev_mat[ind] * TO_MILISECONDS, \
                time_dam_lev_rec_cache[ind] * TO_MILISECONDS))

        ind += 1

    graph_all(time_dam_lev_mat, time_dam_lev_rec, time_dam_lev_rec_cache, time_lev_mat)
    graph(time_dam_lev_mat, time_dam_lev_rec_cache, time_lev_mat)


def main():
    option = -1
    option = int(input(MSG))
    while (option != EXIT):
        if (option == LEV_MAT):
            str1, str2 = input_data()
            print("\nРезультат: ", levenshtein_matrix(str1, str2))

        elif (option == DAM_LEV_MAT):
            str1, str2 = input_data()
            print("\nРезультат: ", damerau_levenshtein_matrix(str1, str2))

        elif (option == DAM_LEV_REC):
            str1, str2 = input_data()
            print("\nРезультат: ", damerau_levenshtein_recursive(str1, str2))

        elif (option == DAM_LEV_REC_CACHE):
            str1, str2 = input_data()
            print("\nРезультат: ", damerau_levenshtein_cache_recursive(str1, str2))

        elif (option == TIME):
            time_measurement()

        else:
            print("\nПовторите ввод\n")

        option = int(input(MSG))


if __name__ == "__main__":
    main()