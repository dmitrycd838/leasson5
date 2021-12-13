# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open("File") as file:
    file_lines = file.readlines()
    print("Количество строк в файле: ", len(file_lines))
    for line_number, line in enumerate(file_lines, 1):
        print(f"Кол-во слов в строке {line_number}:", len(line.split()))