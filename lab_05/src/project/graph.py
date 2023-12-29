import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [1.5238, 3.0126, 4.4944, 5.9263, 7.4181, 8.9156, 10.2940, 11.9333, 13.2111]

y2 = [1.1238, 2.2126, 3.4932, 4.9264, 6.1183, 7.2151, 8.4947, 9.4323, 10.1131]

fig = plt.figure(figsize=(10, 7))
plot = fig.add_subplot()
plt.plot(x, y1, label='Линейная')
plt.plot(x, y2, label='Конвейерная')

plt.xlabel('Количество файлов')
plt.ylabel('Время (в мс)')
plt.title('Временные характеристики')

plt.legend()
plt.grid()
plt.show()


x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
y11 = [1.5238, 2.2589, 3.3409, 4.3925, 5.5193, 6.7832, 7.6820, 8.9341, 9.2402]

y21 = [1.1238, 1.5573, 1.9623, 2.8435, 3.6133, 4.6842, 5.3834, 6.4346, 7.2413]

fig1 = plt.figure(figsize=(10, 7))
plot = fig1.add_subplot()
plt.plot(x1, y11, label='Линейная')
plt.plot(x1, y21, label='Конвейерная')

plt.xlabel('Размер файла')
plt.ylabel('Время (в мс)')
plt.title('Временные характеристики')

plt.legend()
plt.grid()
plt.show()

