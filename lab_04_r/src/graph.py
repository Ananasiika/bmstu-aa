import matplotlib.pyplot as plt 


sizes = [1, 2, 4, 8, 16, 32]
vol = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

posl = [8.21767, 14.934, 23.4654, 30.8813, 37.6075, 46.0016, 55.7736, 64.5141, 72.0826, 78.5542]
paral_100 = [9.15289, 6.40426, 5.5474, 6.10661, 10.914, 19.3397] 
paral_200 = [15.1261, 11.9858, 8.9485, 9.21145, 13.6871, 22.1666] 
paral_300 = [25.5092, 16.8246, 11.1818, 13.506, 17.2514, 24.6682] 
paral_400 = [32.5997, 21.4755, 15.8786, 15.0726, 19.837, 27.9015] 
paral_500 = [38.9155, 25.7524, 18.4156, 18.2228, 21.9657, 31.1922] 
paral_600 = [48.2131, 32.2773, 23.0358, 21.9302, 24.7606, 34.1507] 
paral_700 = [56.3324, 36.5542, 25.5409, 23.5022, 27.5444, 36.3854] 
paral_800 = [65.2434, 40.599, 27.7107, 27.0775, 30.4959, 38.1513] 
paral_900 = [73.4368, 46.1276, 30.308, 27.4626, 32.8594, 42.2644] 
paral_1000 = [78.5421, 51.0476, 33.0593, 31.1097, 35.5935, 43.2498] 

ind = 0

print("Последовательно")
for num in vol:
    print(" %4d & %.2f \\\\ \n \\hline" %(num, \
        posl[ind]
        ))

    ind += 1

ind = 0

print("Параллельно")
for num in sizes:
    print(" %4d & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f \\\\ \n \\hline" %(num, \
        paral_100[ind], paral_200[ind], paral_300[ind], paral_400[ind], \
        paral_500[ind], paral_600[ind], paral_700[ind], paral_800[ind], 
        ))

    ind += 1


fig1 = plt.figure(figsize=(10, 7))
plot = fig1.add_subplot()
plot.plot(sizes, paral_100, label = "Размер - 100кб")
plot.plot(sizes, paral_200, label = "Размер - 200кб")
plot.plot(sizes, paral_300, label = "Размер - 300кб")
plot.plot(sizes, paral_400, label = "Размер - 400кб")
plot.plot(sizes, paral_500, label = "Размер - 500кб")
plot.plot(sizes, paral_600, label = "Размер - 600кб")
plot.plot(sizes, paral_700, label = "Размер - 700кб")
plot.plot(sizes, paral_800, label = "Размер - 800кб")
plot.plot(sizes, paral_900, label = "Размер - 900кб")
plot.plot(sizes, paral_1000, label = "Размер - 1000кб")


plt.legend()
plt.grid()
plt.title("Временные характеристики")
plt.ylabel("Затраченное время (с)")
plt.xlabel("Количество потоков")

plt.show()

stream_2 = [6.38671, 11.3293, 16.8246, 21.4755, 25.7524, 32.2773, 36.5542, 40.599, 46.1276, 51.0476]
stream_4 = [3.68262, 6.15702, 11.1818, 15.8786, 18.4156, 23.0358, 25.5409, 27.7107, 30.308, 33.0593]

fig2 = plt.figure(figsize=(10, 7))
plot = fig2.add_subplot()
plot.plot(vol, posl, label = "Последовательно")
plot.plot(vol, stream_2, label = "2 потока")
plot.plot(vol, stream_4, label = "4 потока")


plt.legend()
plt.grid()
plt.title("Временные характеристики")
plt.ylabel("Затраченное время (с)")
plt.xlabel("Размер файла (в кб)")

plt.show()
