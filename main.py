# получает на вход введенную пользователем строку с примером
# выдает на выход последнюю запись из журнала логов

import controller



def enter():
    data = input("Enter a calculation: ")
    with open ('save_enter.txt', 'w') as file:
        file.write(data)
    return data
 
def log():
    
    with open ('log.csv', 'r') as file1:
        log = file1.read()
    return log


print(enter())
print(log())