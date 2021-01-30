# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open("data/HW5.4.txt", 'r') as file:
    new_text = []
    for line in file:
        line = line.replace('—', '')
        text_number, num = line.split()
        new_line = f'{dict[text_number]} — {num}\n'
        new_text.append(new_line)
    new_text[-1] = new_text[-1].rstrip('\n')  # чтобы не было пустой строки в файле

with open('data/HW5.4(ru).txt', 'w') as file:
    file.writelines(new_text)

# Проверка
with open('data/HW5.4(ru).txt', 'r') as file:
    data=file.read()
print(data)