import os

# Функция для чтения файла и получения его имени, количества строк и содержимого
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return file_name, len(lines), lines

# Список файлов для объединения
file_names = ['1.txt', '2.txt', '3.txt']  # Укажите ваши файлы здесь

# Список для хранения информации о файлах (имя, количество строк, содержимое)
file_info = []

# Чтение всех файлов
for file_name in file_names:
    if os.path.exists(file_name):
        file_info.append(read_file(file_name))
    else:
        print(f"Файл {file_name} не существует!")

# Сортировка файлов по количеству строк
file_info.sort(key=lambda x: x[1])

# Запись результата в итоговый файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, num_lines, lines in file_info:
        # Запись имени файла и количества строк
        result_file.write(f"\n{file_name}\n{num_lines}\n")
        # Запись содержимого файла
        result_file.writelines(lines)