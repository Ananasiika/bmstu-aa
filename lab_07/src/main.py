from time import process_time_ns
import matplotlib.pyplot as plt 
from copy import deepcopy
import random
import string


from algorithms import bm_search, kmp_search, bm_search_count_comparisons, kmp_search_count_comparisons


MSG = "\n\n Алгоритмы поиска \n\n \
    1. Алгоритм Кнута-Морриса-Пратта \n \
    2. Модифицированный алгоритм с введением эвристики \"плохого\" символа \n \
    3. Оба алгоритма \n \
    4. Замерить время \n \
    5. Проанализировать кол-во сравнений \n \
    0. Выход \n\n \
    \
    Выбор: \
    "

# Define
EXIT = 0
KNUT= 1
MOD = 2
ALL_SEARCH = 3
TIME_MEASURE =  4
TEST_comparisonS = 5
SHOW_DATA = 6

# Type
LATEX = 0
CSV = 1
NORMAL = 2

TIMES = 250
TO_MICROSECONDS = 1000


def get_process_time(func, text, pat):
    
    time_res = 0

    for _ in range(TIMES):
        text_cur = deepcopy(text)
        pattern = deepcopy(pat)

        time_start = process_time_ns()
        func(text_cur, pattern)
        time_end = process_time_ns()

        time_res += (time_end - time_start) / TO_MICROSECONDS


    return time_res / TIMES


def time_test():
    ind_keys = [ind for ind in range(28)]
    kmp_time = []
    bm_time = []

    print()

    for ind in ind_keys:
        kmp, bm = 0, 0
        for it in range(TIMES):
            letters = string.ascii_letters + string.digits
            text = ''.join(random.choice(letters) for _ in range(50))
            key = text[ind] + text[ind+1] + text[ind+2]
            kmp += get_process_time(kmp_search, text, key)
            bm += get_process_time(bm_search, text, key)

        kmp_time.append(kmp / TIMES)
        bm_time.append(bm / TIMES)

    kmp, bm = 0, 0
    for it in range(TIMES):
        letters = string.ascii_letters + string.digits
        text = ''.join(random.choice(letters) for _ in range(50))
        key = "1_2"
        kmp += get_process_time(kmp_search, text, key)
        bm += get_process_time(bm_search, text, key)

    kmp_time.append(kmp / TIMES)
    bm_time.append(bm / TIMES)

    # Graph
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(ind_keys + ["-1"], kmp_time, label = "Алгоритм Кнута-Морриса-Пратта")
    plot.plot(ind_keys + ["-1"], bm_time, label="Модифицированный алгоритм")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (мкс)")
    plt.xlabel("Индекс ключа")
    
    plt.show()


def comparison_test():

    alg = int(input("\nВыберите алгоритм: \
                \n\t1. Алгоритм Кнута-Морриса-Пратта \
                \n\t2. Модифицированный алгоритм с введением эвристики \"плохого\" символа \
                \n\nВыбор: "))

    alg_text = "Не определено"
    
    if (alg == KNUT):
        alg_text = "Алгоритм Кнута-Морриса-Пратта"
    elif (alg == MOD):
        alg_text = "Модифицированный алгоритм"
    else:
        print("\nОшибка: Неверно выбран алгоритм\n")
        return

    text = "1234567890asdfghjklzxcvbnmqwertyuio"

    ind_keys = [ind for ind in range(len(text) - 1)]


    keys = [text[i] + text[i+1] + text[i+2] for i in range(len(text) - 2)] + ['p']

    search_comparisons = []

    percentage = 0
    all_percentage = len(text)
    print()

    for key in keys:
        percentage += 1

        if (alg == KNUT):
            search_comparisons.append(kmp_search_count_comparisons(text, key))
        elif (alg == MOD):
            search_comparisons.append(bm_search_count_comparisons(text, key))

        if (percentage % 50 == 0):
            print("Progress: %5.2f%s (key = %s)" %((percentage / all_percentage) * 100, "%", key))


    # Graph
    fig, ax = plt.subplots(1, 1, figsize = (10, 7))

    ax.bar(ind_keys[0:32], search_comparisons[1:33], alpha=0.5)
    ax.bar(len(ind_keys), search_comparisons[33], alpha=0.5)
    ax.text(len(ind_keys), -1, "-1", ha="center", va="center")

    ax.set(title="График количества сравнений\n" + alg_text)

    ax.set_xlabel("Индекс ключа")
    ax.set_ylabel("Количество сравнений")
    ax.set_xticks(list(range(0, len(ind_keys) - 2)))
    #ax.set_xticklabels(list(range(0, len(ind_keys) - 2)) + ["-1"])

    ax.grid()
    ax.legend()

    plt.show()


def main():
    option = -1

    while (option != EXIT):
        option = int(input(MSG))

        if (option == KNUT):

            text = input("\nВведите строку: ")
            pattern = input("\nВведите подстроку: ")

            ans = kmp_search(text, pattern)
            print(ans)

        elif (option == MOD):

            text = input("\nВведите строку: ")
            pattern = input("\nВведите подстроку: ")

            ans = bm_search(text, pattern)
            print(ans)

        elif (option == ALL_SEARCH):

            text = input("\nВведите строку: ")
            pattern = input("\nВведите подстроку: ")

            ans1 = kmp_search(text, pattern)
            ans2 = bm_search(text, pattern)
            print("Алгоритм Кнута-Морриса-Пратта:", ans1)
            print("Модифицированный алгоритм:", ans2)

        elif (option == TIME_MEASURE):

            time_test()

        elif (option == TEST_comparisonS):

            comparison_test()

        else:
            print("\nПовторите ввод\n")


if __name__ == "__main__":
    main()
