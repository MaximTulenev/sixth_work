import random
number = random.randint(1, 10)
guess_number = int(input("Введите целое число от 1 до 10: "))
while guess_number != number:
    print("Неверное число. Попробуйте заново.")
    int(input("Введите целое число от 1 до 10: "))
    break
print("Поздравляю! Вы отгадали загаданое число.")
