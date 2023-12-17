from time import process_time_ns
from random import randint
import matplotlib.pyplot as plt 
from algorythms import standart_alg, vinograd_alg, optimized_vinograd_alg, strassen_alg, memory_standart_alg, memory_vinograd_alg, memory_optimized_vinograd_alg, memory_strassen_alg

MSG = "\n\n      Меню \n\n \
    1. Станадартное умножение матриц \n \
    2. Алгоритм Винограда \n \
    3. Оптимизированный алгоритм Винограда \n \
    4. Алгоритм Штрассена \n \
    5. Все алгоритмы \n \
    6. Замеры времени \n \
    0. Выход \n\n \
    \
    Выбор: \
    "

EXIT = 0
STD_ALG = 1
VIN_ALG = 2
VIN_OPT_ALG = 3
SHT_ALG = 4
ALL_ALG = 5
TIME = 6

TIMES = 100
TO_MILISECONDS = 1000


def input_matrix():
    try:
        row = int(input("\nВведите количество строк: \t"))
        col = int(input("Введите количество столбцов: \t"))

        if ((row < 1) or (col < 1)):
            print("Ошибка: Должно быть больше 1")
            return []
    except:
        print("Ошибка: Введено не число")
        return []

    print("\nВведите матрицу по строчно (в одной строке - все числа для данной строки матрицы): ")
    matrix = []

    for _ in range(row):
        tmp_arr = list(int(i) for i in input().split())

        if (len(tmp_arr) != col):
            print("Ошибка: Количество чисел не соответствует количеству столбцов матрицы")
            return []

        matrix.append(tmp_arr)

    return matrix
        

def output_matrix(matrix, msg):

    print(msg + '\n')

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            print("%-4d" %(matrix[i][j]), end = '')

        print()


def input_data():
    mat_a = input_matrix()
    mat_b = input_matrix()

    return mat_a, mat_b


def get_rand_matrix(size):
    
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            matrix[i][j] = randint(0, 50)

    return matrix


def get_process_time(func, size):
    
    time_res = 0

    for _ in range(TIMES):
        mat_a = get_rand_matrix(size)
        mat_b = get_rand_matrix(size)

        time_start = process_time_ns()
        func(mat_a, mat_b)
        time_end = process_time_ns()

        time_res += (time_end - time_start) / TO_MILISECONDS / TO_MILISECONDS


    return time_res / TIMES


def test_algos():

    for_test = [2, 4, 8, 10, 15, 16, 20, 25, 30, 32, 35, 40, 45, 50, 55, 60, 64, 65, 70, 75]

    time_std_alg = []
    time_vin_alg = []
    time_vin_alg_opt = []
    time_sht_alg = []

    for num in for_test:

        print("Progress:", num, "len \r")

        time_std_alg.append(get_process_time(standart_alg, num))
        time_vin_alg.append(get_process_time(vinograd_alg, num))
    #    time_vin_alg_opt.append(get_process_time(optimized_vinograd_alg, num))
    #     time_sht_alg.append(get_process_time(strassen_alg, num))

    # print("\n\nЗамер времени для алгоритмов: \n")

    # ind = 0

    # for num in for_test:
    #     print(" %4d & %.4f & %.4f & %.4f & %.4f \\\\ \n \\hline" %(num, \
    #         time_std_alg[ind] * TO_MILISECONDS, \
    #         time_vin_alg[ind] * TO_MILISECONDS, \
    #         time_vin_alg_opt[ind] * TO_MILISECONDS, \
    #         time_sht_alg[ind] * TO_MILISECONDS, ))

    #     ind += 1


    # fig = plt.figure(figsize=(10, 7))
    # plot = fig.add_subplot()
    # plot.plot(for_test, time_std_alg, label = "Стандартный алгоритм")
    # plot.plot(for_test, time_vin_alg, label="Алгоритм Винограда")
    # plot.plot(for_test, time_vin_alg_opt, label="Оптимизированный алгоритм Винограда")
    # plot.plot(for_test, time_sht_alg, label="Алгоритм Штрассена")
    # plot.semilogy()
    # plt.legend()
    # plt.grid()
    # plt.title("Временные характеристики")
    # plt.ylabel("Затраченное время (мкс)")
    # plt.xlabel("Размер")
    # plt.show()

    fig = plt.figure(figsize=(10, 7))
    plot2 = fig.add_subplot()
    plot2.plot(for_test, time_vin_alg, label = "Алгоритм Винограда")
    plot2.plot(for_test, time_std_alg, label="Стандартный алгоритм")
    plot2.semilogy()
    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (мкс)")
    plt.xlabel("Размер")
    plt.show()

def memory():
    for_test = [2, 4, 8, 10, 15, 16, 20, 25, 30, 32, 35, 40, 45, 50, 55, 60, 64]
    mem_std_alg = []
    mem_vin_alg = []
    mem_vin_alg_opt = []
    mem_sht_alg = []

    for num in for_test:
        mat_a = get_rand_matrix(num)
        mat_b = get_rand_matrix(num)
        print("Progress:", num, "len \r")

        mem_std_alg.append(memory_standart_alg(mat_a, mat_b))
        mem_vin_alg.append(memory_vinograd_alg(mat_a, mat_b))
        mem_vin_alg_opt.append(memory_optimized_vinograd_alg(mat_a, mat_b))
        mem_sht_alg.append(memory_strassen_alg(mat_a, mat_b))

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(for_test, mem_std_alg, label = "Стандартный алгоритм")
    plot.plot(for_test, mem_vin_alg, label="Алгоритм Винограда")
    plot.plot(for_test, mem_vin_alg_opt, label="Оптимизированный алгоритм Винограда")
    plot.plot(for_test, mem_sht_alg, label="Алгоритм Штрассена")
    plt.legend()
    plt.grid()
    plt.title("Характеристики памяти")
    plt.ylabel("Память")
    plt.xlabel("Размер")
    plt.show()


def main():
    option = -1

    option = int(input(MSG))
    while (option != EXIT):

        if (option == STD_ALG):

            mat_a, mat_b = input_data()

            res = standart_alg(mat_a, mat_b)

            output_matrix(res, "\n\nРезультат:")

        elif (option == VIN_ALG):

            mat_a, mat_b = input_data()

            res = vinograd_alg(mat_a, mat_b)

            output_matrix(res, "\n\nРезультат:")

        elif (option == VIN_OPT_ALG):

            mat_a, mat_b = input_data()

            res = vinograd_alg(mat_a, mat_b)

            output_matrix(res, "\n\nРезультат:")

        elif (option == SHT_ALG):
            
            mat_a, mat_b = input_data()

            res = strassen_alg(mat_a, mat_b)

            output_matrix(res, "\n\nРезультат:")

        elif (option == ALL_ALG):

            mat_a, mat_b = input_data()

            res_std = standart_alg(mat_a, mat_b)
            res_vin = vinograd_alg(mat_a, mat_b)
            res_vin_opt = optimized_vinograd_alg(mat_a, mat_b)
            res_sht = strassen_alg(mat_a, mat_b)

            output_matrix(res_std, "\n\nРезультат стандартаного алгоритма:")
            output_matrix(res_vin, "\n\nРезультат алгоритма Винограда:")
            output_matrix(res_vin_opt, "\n\nРезультат оптимизированного алгоритма Винограда:")
            output_matrix(res_sht, "\n\nРезультат алгоритма Штрассена:")

        elif (option == TIME):
            
            test_algos()

        else:
            print("\nПовторите ввод\n")

        option = int(input(MSG))


if __name__ == "__main__":
    main()
