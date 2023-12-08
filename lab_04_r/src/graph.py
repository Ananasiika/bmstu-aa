import matplotlib.pyplot as plt 


sizes = [1, 2, 4, 8, 16, 32]
vol = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

posl = [2.88409, 4.27489, 5.75491, 7.26732, 8.75398, 10.1951, 11.7365, 13.587,  15.1489, 16.8682]
paral_100 = [2.81264, 2.27958, 2.71939, 4.56004, 8.595, 16.6329] 
paral_200 = [4.9027, 3.69842, 3.88657, 5.1954, 9.20223, 17.2244] 
paral_300 = [7.74852, 5.07647, 4.57447, 6.18979, 10.227, 17.9048] 
paral_400 = [8.4502, 6.01617, 4.97891, 6.44757, 10.4843, 18.702] 
paral_500 = [9.54212, 6.64862, 5.54788, 7.01544, 11.0783, 19.0995] 
paral_600 = [11.4077, 7.78886, 6.17074, 7.60125, 11.8962, 19.7545] 
paral_700 = [13.1234, 8.90301, 6.8247, 8.23345, 12.2513, 20.2258] 
paral_800 = [13.6768, 9.59123, 7.66636, 8.91679, 12.8844, 20.9122] 
paral_900 = [16.5969, 10.9609, 8.32399, 9.53008, 13.5321, 21.7051] 
paral_1000 = [19.3428, 11.9121, 8.95415, 10.1271, 14.3074, 22.4866] 

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

stream_2 = [2.27958, 3.69842, 5.07647, 6.01617, 6.64862, 7.78886, 8.90301, 9.59123, 10.9609, 11.9121]
stream_4 = [2.71939, 3.88657, 4.57447, 4.97891, 5.54788, 6.17074, 6.8247, 7.66636, 8.32399, 8.95415]

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
