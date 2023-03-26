from datetime import datetime
from progress.bar import Bar
from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge

dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

bar = Bar('Processing', max=20)
for i in range(20):
    #какая то работа
    bar.next()
bar.finish()

while True:
    com = input('Введите номер нужной функции: ')
    if com == '1':
        cs()
        print(dt)
        break
    elif com == '2':
        ge()
        print(dt)
        break
    else:
        break