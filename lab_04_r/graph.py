import matplotlib.pyplot as plt 


sizes = [1, 2, 4, 8, 16, 32]

posl = [3.01155, 4.34946, 6.04471, 7.63111, 9.3657, 11.0387, 12.498, 14.029, 15.7239, 17.3401]
paral_100 = [2.9117, 2.7764, 2.99504, 4.54476, 8.52977, 16.4531] 
paral_200 = [3.56046, 2.76188, 2.97586, 4.56249, 8.53759, 16.4416] 
paral_300 = [3.60095, 2.75594, 2.97705, 4.54385, 8.56008, 16.4378] 
paral_400 = [3.57147, 2.77471, 3.00336, 4.55745, 8.52298, 16.6219] 
paral_500 = [2.91034, 2.76395, 2.96558, 4.54914, 8.54106, 16.4797] 
paral_600 = [3.5627, 2.74562, 2.99029, 4.54783, 9.34693, 18.355] 
paral_700 = [4.33306, 3.16789, 3.17112, 4.96116, 9.0402, 17.2283] 
paral_800 = [3.80013, 2.80748, 3.26433, 4.84403, 9.18345, 19.4577] 
paral_900 = [4.01853, 3.00637, 3.20399, 4.97079, 9.13595, 17.1964] 
paral_1000 = [3.95444, 2.98985, 3.1486, 4.86131, 8.92779, 17.1664] 

ind = 0

print("Последовательно")
for num in sizes:
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
