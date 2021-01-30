# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
# Создаем папку data для дальнейшей работы
# import  os
# if not os.path.isdir("data"):
#      os.mkdir("data")

def create_file():

    with open("data/text.txt", "w") as txt_file:
        while True:
            user_txt = input("Введите строку для записи её в файл.\n"
                             "Оставьте строку пустой и нажмите Enter, чтобы совершить выход.\n")
            if user_txt != "":
                txt_file.write("".join([user_txt, "\n"]))
            else:
                break

create_file()