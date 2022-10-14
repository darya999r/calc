# переводит строку в удобный формат для рассчета
# определяет, в какой модуль на рассчет отправить

# import main
import racio
import complex


def conversion ():
    with open ('save_enter.txt', 'r') as file:
        data_1 = file.read()
    data_1 = list(data_1)
    return data_1

def separator (data_1):
    # здесь выбираем где считать в racio or complex
    a = "."
    b = "i"
    # for _ in data_1:
    if a in data_1: 
        sep = 'racio'
        result = racio.result(data_1)
    elif b in data_1: 
        sep = 'complex'
        result = complex.result(data_1)
    else: 
        sep = 'input error'
        result = None
        print("Error")
    with open('save_sep.txt', 'w') as file:
        file.write(sep)
    return result


data_convers = conversion()
print(data_convers)
res = complex.result(data_convers)
print(res)
