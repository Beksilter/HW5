# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summ():
    try:
        with open("data/HW5.5.txt", 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка, попробуйте снова, введите целое число')
    except TypeErrorError:
        print("Попробуйте снова, введите численные значения")
summ()