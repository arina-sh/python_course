S = 0 # переменная для подсчёта суммы
while True:
    try:
        num_of_tickets = int(input('Введите количество билетов: '))
        if num_of_tickets > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print('Вы ввели неправильное значение.\nВведите положительное целое число.')
for i in range(1, num_of_tickets + 1):
    while True:
        try:
            age = int(input(f'Введите возраст посетителя {i}: '))
            if age <= 0 or age > 120:
                raise ValueError('Вам не может быть столько лет.')
            elif 0 < age < 18:
                print('Билет  - бесплатный')
                print(f'Промежуточная сумма (+ 0 руб.): {S} руб.')
            elif 18 <= age < 25:
                S += 990
                print(f'Промежуточная сумма (+ 990 руб.): {S}')
            else:
                S += 1390
                print(f'Промежуточная сумма к оплате(+ 1390 руб.): {S} руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Вы ввели неправильное значение.\nВведите положительное целое число.')

if num_of_tickets > 3:
    print(f'Сумма к оплате со скидкой 10%: {S - 0.1 * S} руб.')
else:
    print(f'Сумма к оплате (без скидки): {S} руб.')