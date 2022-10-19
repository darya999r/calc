import controller as ctrl
import logger as log

# Стартовое меню

def start():
    print("Привет!", "Это наш калькулятор!", "Может посчитать арифметичесое выражение либо с рациональными, либо с комплексными числами.", sep = "\n")
    while True:
        command = input("Выберите дальнейшее действие или обратитесь в /help: ")
        if command == "/help":
            print("/enter - ввод арифмитического выражения", "/log - просмотр данных логирования", "/clear - очистка лог-файла", "/stop - завершить работу", sep = "\n")
        elif command == "/enter":
            expression = str(input("Введите арифметическое выражение: "))
            chek(expression)
        elif command == "/log":
            log.view_log()
        elif command == "/clear":
            log.clear_log()
            print("Файл логирования очищен.")
        elif command == "/stop":
            print("Будем рады видеть Вам снова!")
            break

def chek(expression):
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '^', '(', ')', 'i', 'j', ' ', '.']
    for i in range(len(expression)):
        if expression[i] not in values:
            print ("Выражение задано некорректно. Попробуйте ещё раз.")
            start()
    ctrl.separator(expression)

start()