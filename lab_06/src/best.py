import re
# Укажите путь к файлу
file_path = "./parametrization_class2.txt"

# Открываем файл для чтения
with open(file_path, "r") as file:
    # Читаем строки из файла
    lines = file.readlines()
    
# Итерируемся по строкам
for line in lines:
    # Разделяем строку по разделителям (в данном случае "&")
    values = re.split(r"&|\\\\", line)
    # Удаляем начальные и конечные пробелы из каждого значения
    values = [value.strip() for value in values]
    
    # Проверяем, равно ли последнее значение нулю
    if values[-2] == "0":
        # Выводим строку
        print(line.strip())
        print("\hline")
