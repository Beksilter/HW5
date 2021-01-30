# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
# Используем уже созданный в первом пункте файл.
with open("data/text.txt", encoding='utf-8') as f:
    list_lines = f.readlines()
    print(f"В данном файле {len(list_lines)} строк(и).")

with open("data/text.txt", 'r', encoding='utf-8') as f:
    for ind, line in enumerate(f, 1):
        not_count = [',','\n','.','"','!',';',':','?',"'",'+','-','*','/','=','_']  #Убираем из подсчета слов знаки, но если нужно что-то оставить, то легко изменить
        for el in not_count:
            line = line.replace(el, '')
        words_amount = len(line.split())
        print(f'Строка {ind}: количество слов {words_amount}')


