from random import randint

HELP_TEXT = """
«Угадай число» — это игра, в которой игрок должен угадать число, 
которое случайным образом выбирается компьютером из диапазона от 1 до 100 включительно.
Правила игры:
Компьютер случайным образом выбирает число в указанном диапазоне.
Игрок вводит в терминале своё предположение относительно этого числа.
Программа сравнивает выбор игрока с загаданным числом.
Если предположение оказалось неверным, программа предложит попробовать снова.
Игра будет продолжаться, пока игрок не угадает загаданное число.
"""
rundom_number = randint(1, 100)

def get_number():
    while True:
        number = input("Введите число от 1 до 100: ")
        if str.isdigit(number) and 1 <= int(number) <= 100:
            return int(number)
        elif number == "help":
            print(HELP_TEXT)
        elif number == "exit":
            print("Спасибо, возвращайтесь к нам снова")
            exit(0)
        else:
            print("Некорректное значение - попробуйте снова")

def run():
    while True:
        number = get_number()
        if number < rundom_number:
            print("Ваше число меньше того, что загадано")
        elif number > rundom_number:
            print("Ваше число больше того, что загадано")
        elif number == rundom_number:
            print("Отличная интуиция! Вы угадали число :)")
            break

#if __name__ == "main":
#    run()
run()