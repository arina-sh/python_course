per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую планируете положить под проценты: '))

deposit = []
for i in per_cent.values():
    deposit.append(int(i * money / 100))
print(deposit)

print('Максимальная сумма, которую вы можете заработать — ' + str(max(deposit)))