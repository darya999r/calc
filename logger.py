# записывает данные с каждого используемого модуля в журнал
# выдает последнюю запись из журнала логов


from datetime import datetime as dt
import main
import controller



def datetime (data,sep,res):
    data = main.enter()
    data_1 = controller.conversion()
    with open('save_sep.txt', 'r') as file:
        sep = file.read()
    res = controller.separator(data_1)
    time = dt.now().strftime('%d/%M/%Y %H:%M')
    with open ('log.csv', 'a') as file:
        file.write('DateTime:{},Calculation:{},DataType:{},Result:{}\n'.format(time,data,sep,res))






