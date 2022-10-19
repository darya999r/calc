from datetime import datetime as dt

def datetime (data,res):
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    with open ('log.csv', 'a') as file:
        file.write('DateTime:{}, Calculation:{}, Result:{}\n'.format(time,data,res))

def view_log():
    with open('log.csv', 'r') as data:
        for line in data:
            print(line)

def clear_log():
    data = open ('log.csv', 'w')
    data.close()